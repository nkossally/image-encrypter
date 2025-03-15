import React, { useState } from "react";
import { API_URL } from "../config";
import ProgressBar from "./ProgressBar";
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

  const hexLetters = "abcdefABCDEF0123456789"

  const getHexKeyInputIsValid = () =>{
    if(inputText.length !== 32) return false;
    for(let i = 0; i < inputText.length; i++){
      if(!hexLetters.includes(inputText[i])){
        console.log("bad letter")
        return false
      }
    }
    return true
  }
  
  const getCanSubmit = () =>{
    if( isDecryption && !getHexKeyInputIsValid()) return false
    if(!image) return false
    return true
  }

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setImage(file);
      setPreview(URL.createObjectURL(file)); // Generate preview URL for image
    }
  };

  const handleInputChange = (e) => {
    setInputText(e.target.value);
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
          {!isLoading && (
            <input
              className={classNames("file-input", "fade-in")}
              type="file"
              accept="image/*"
              onChange={handleImageChange}
            />
          )}

          {/* Image preview */}
          {preview && image && !isLoading && (
            <img
              src={preview}
              alt="Image preview"
              style={{ width: "200px", height: "auto" }}
              className="fade-in"
            />
          )}
            {isDecryption && !isLoading && (
              <input className={classNames("key-input", "fade-in")} placeholder="enter key" onChange={handleInputChange} />
            )}

            {/* Button to upload image */}
            {image && !isLoading &&  getCanSubmit() && (
              <button className={classNames("upload-button","fade-in")} disabled={!getCanSubmit()} onClick={handleImageEncryption}>
                Upload Image
              </button>
            )}
            {isLoading && <Spinner />}

            {/* {isLoading && <ProgressBar isDecryption={isDecryption} />} */}
        </div>
      )}
    </>
  );
};

export default ImageUpload;
