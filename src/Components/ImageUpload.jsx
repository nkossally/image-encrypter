import React, { useState, useEffect } from "react";
import { API_URL } from "../config";
import ProgressBar from "./ProgressBar";
import FileInput from "./FileInput";
import Spinner from "./Spinner";
import Result from "./Result";
import classNames from "classnames" 

const ImageUpload = ({ isDecryption }) => {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [inputText, setInputText] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [showResult, setShowResult] = useState(false);
  const [url, setUrl] = useState("");
  const [hexKey, setHexKey] = useState("")
  const [error, setError] = useState("");
  const [responseMessage, setResponseMessage] = useState("");
  const [validationError, setValidationError] = useState(false)

  const hexLetters = "abcdefABCDEF0123456789"

  const getHexKeyInputIsValid = (currInput, shouldSetErrors) => {
    if(currInput.length !== 32){
      if(shouldSetErrors) setValidationError("Key must have 32 characters.")
      return false
    }
    for(let i = 0; i < currInput.length; i++){
      if(!hexLetters.includes(currInput[i])){
       if(shouldSetErrors) setValidationError("Key contains an invalid character.")
        return false
      }
    }
    if(shouldSetErrors) setValidationError("")
    return true
  }
  
  const getCanSubmit = (shouldSetErrors) => {

    if( isDecryption && !getHexKeyInputIsValid(inputText, shouldSetErrors)){
      return false
    }
    if(!image){
      return false;
    }
    if(shouldSetErrors) setValidationError("")
    return true
  }

  const handleImageChange = (file) => {
    if (file) {
      setImage(file);
      setPreview(URL.createObjectURL(file)); // Generate preview URL for image
    }
  };

  const handleInputChange = (e) => {
    setInputText(e.target.value);
    getHexKeyInputIsValid(e.target.value, true)
  };

  const handleImageEncryption = async () => {
    setError("");
    setResponseMessage("");
    setUrl("");
    setHexKey("")

    const formData = new FormData();
    formData.append("image", image);
    formData.append("key", inputText);

    let endpoint = isDecryption ? "/decrypt" : "/encrypt";
    // endpoint = "/test"

    try {
      setIsLoading(true);
      const response = await fetch(`${API_URL}${endpoint}`, {
        method: "POST",
        body: formData,
      });
      const json = await response.json();
      setIsLoading(false);
      if(json["error"]){
        setError(json["error"])
      }

      setResponseMessage(json["message"]);
      setUrl(json["url"]);
      setHexKey(json["key"])

      setShowResult(true);
      
    } catch (err) {
      setIsLoading(false);
      setError(`Failed to upload and ${isDecryption ? "decrypt" : "encrypt"} image. Try encrypting a smaller image.`);
      setShowResult(true);
    }
  };

  const goBack = () =>{
    setShowResult(false)
    setError("")
  }

  return (
    <>
      {showResult && (
        <Result
          hexKey={hexKey}
          error={error}
          goBack={goBack}
          url={url}
          responseMessage={responseMessage}
        />
      )}
      {!showResult && (
        <div className="form">
          {/* File input for image */}

          {!isLoading && <FileInput handleImageChange={handleImageChange} />}

          {/* Image preview */}
          {preview && image && !isLoading && (
            <img
              src={preview}
              alt="Image preview"
              style={{ width: "200px", height: "auto" }}
              className="fade-in"
            />
          )}
          <div className={classNames("validation-error", "fade-in")}>
            {" "}
            {validationError}{" "}
          </div>
          {isDecryption && !isLoading && (
            <input
              className={classNames("key-input", "fade-in")}
              placeholder="enter key"
              onChange={handleInputChange}
            />
          )}

          {/* Button to upload image */}
          {image && !isLoading && getCanSubmit(false) && (
            <button
              className={classNames("styled-button", "fade-in")}
              disabled={!getCanSubmit(false)}
              onClick={handleImageEncryption}
            >
              Submit Image
            </button>
          )}
          {/* {isLoading && <Spinner />} */}

          {isLoading && <ProgressBar isDecryption={isDecryption} />}
        </div>
      )}
    </>
  );
};

export default ImageUpload;
