import React, { useState, useEffect } from 'react';
import Pusher from 'pusher-js';

const ProgressBar = ({ isDecryption }) => {
  const [progress, setProgress] = useState(0);

  useEffect(() => {
    const pusher = new Pusher("0f67a7553357ff1f8491", {
      cluster: "us3",
      encrypted: true,
    });
    const channel = pusher.subscribe("progress_update");
    channel.bind("progress_update", (data) => {
      setProgress(data.progress);
    });
    return () => {
      pusher.unsubscribe("progress_update");
    };
  }, []);


  return (
    <div className="fade-in">
      {progress < 100 && (
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
