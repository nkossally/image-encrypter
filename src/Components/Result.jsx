import React from "react";

const Result = ({ url, setShowResult, responseMessage, hexKey, error }) => {
    return (
    <div>
      <button onClick={() => setShowResult(false)}>Back</button>
      {responseMessage && <div>{responseMessage}</div>}
      {error && <div>{error}</div>}
      {url && (
        <a href={url} target="_blank">
          Image Link
        </a>
      )}
      {hexKey && <div>Use this key for decryption: {hexKey} </div>}
    </div>
  );
};

export default Result;
