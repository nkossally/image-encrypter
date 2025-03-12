import React from "react";

const Result = ({ url, setShowResult, responseMessage, hexKey, error }) => {
    console.log("error", error)
    return (
    <div>
      <button className="vertical-margin" onClick={() => setShowResult(false)}>Back</button>
      {responseMessage && <div className="vertical-margin">{responseMessage}</div>}
      {error && <div className="vertical-margin">{error}</div>}
      {url && (
        <a href={url} className="vertical-margin" target="_blank">
          Image Link
        </a>
      )}
      {hexKey && <div className="vertical-margin">Use this key for decryption: {hexKey} </div>}
    </div>
  );
};

export default Result;
