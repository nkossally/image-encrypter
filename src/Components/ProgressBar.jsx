import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';
import { API_URL } from "../config";

const ProgressBar = ({isDecryption}) => {
  const [progress, setProgress] = useState(0);
  const [isTaskRunning, setIsTaskRunning] = useState(false);

  useEffect(() => {
    const socket = io(API_URL);  // Connect to Flask backend
    
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
    fetch(`${API_URL}/start-task`)  // Start the task from Flask
      .then((response) => response.json())
      .then((data) => console.log(data.message));
  };


  return (
    <div>
      { progress > 0 && progress < 100 && (
        <div>
          <h3 className="progress-bar-label"> {isDecryption ? "Decryption " : "Encryption"}Progress: {progress}%</h3>
          <progress value={progress} max="100"></progress>
        </div>
      )}
    </div>
  );
};

export default ProgressBar;
