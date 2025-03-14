import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';

const ProgressBar = () => {
  const [progress, setProgress] = useState(0);
  const [isTaskRunning, setIsTaskRunning] = useState(false);

  useEffect(() => {
    const socket = io('http://localhost:8000');  // Connect to Flask backend
    
    // Listen for progress updates from the backend
    socket.on('progress_update', (data) => {
      setProgress(data.progress);
      if (data.progress === 100) {
        setIsTaskRunning(false);  // Task is complete
      }
    });

    return () => {
      socket.disconnect();  // Cleanup when the component unmounts
    };
  }, []);

  const startTask = () => {
    setIsTaskRunning(true);
    fetch('http://localhost:8000/start-task')  // Start the task from Flask
      .then((response) => response.json())
      .then((data) => console.log(data.message));
  };

  return (
    <div>
      <button onClick={startTask} disabled={isTaskRunning}>
        Start Task
      </button>
      {isTaskRunning && (
        <div>
          <h3>Progress: {progress}%</h3>
          <progress value={progress} max="100"></progress>
        </div>
      )}
    </div>
  );
};

export default ProgressBar;
