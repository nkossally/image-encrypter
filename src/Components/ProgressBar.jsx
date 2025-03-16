import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';
import Pusher from 'pusher-js';
import { API_URL } from "../config";

const ProgressBar = ({ isDecryption }) => {
  const [progress, setProgress] = useState(0);
  const [isTaskRunning, setIsTaskRunning] = useState(false);

  useEffect(() => {
    const pusher = new Pusher("0f67a7553357ff1f8491", {
      cluster: "us3",
      encrypted: true,
    });
    const channel = pusher.subscribe("progress_update");
    channel.bind("progress_update", (data) => {
      setProgress(data.progress);
      if (data.progress === 100) {
        setIsTaskRunning(false); // Task is complete
      }
      console.log(data)
    });
    return () => {
      pusher.unsubscribe("progress_update");
    };
  }, []);

  // useEffect(() => {
  //   const socket = io(API_URL); // Connect to Flask backend

  //   // Listen for progress updates from the backend
  //   socket.on("progress_update", (data) => {
  //     setProgress(data.progress);
  //     if (data.progress === 100) {
  //       setIsTaskRunning(false); // Task is complete
  //     }
  //   });

  //   return () => {
  //     socket.disconnect(); // Cleanup when the component unmounts
  //   };
  // }, []);


  return (
    <div className="fade-in">
      {progress > 0 && progress < 100 && (
        <div>
          <h3 className="progress-bar-label">
            {" "}
            {isDecryption ? "Decryption " : "Encryption"}Progress: {progress}%
          </h3>
          <progress value={progress} max="100"></progress>
        </div>
      )}
    </div>
  );
};

export default ProgressBar;
