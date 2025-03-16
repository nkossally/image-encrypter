import React from "react";
import classNames from "classnames"
const Result = ({ url, goBack, responseMessage, hexKey, error }) => {
    return (
    <div>
      <button className={classNames("vertical-margin", "fade-in", "styled-button-small")} onClick={goBack}>Back</button>
      {responseMessage && <div className={classNames("vertical-margin", "fade-in")}>{responseMessage}</div>}
      {error && <div className={classNames("vertical-margin", "fade-in")}>{error}</div>}
      {url && (
        <a href={url} className={classNames("vertical-margin", "fade-in")} target="_blank">
          Image Link
        </a>
      )}
      {hexKey && <div className={classNames("vertical-margin", "fade-in")}>Use this key for decryption: {hexKey} </div>}
    </div>
  );
};

export default Result;
