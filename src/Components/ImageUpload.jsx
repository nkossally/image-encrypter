import React, { useState } from "react";
import { API_URL } from "../config";
import Spinner from "./Spinner";
import Result from "./Result";

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

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setImage(file);
      setPreview(URL.createObjectURL(file)); // Generate preview URL for image
    }
  };

  const handleInputChange = (e) => {
    setInputText(e.target.value);
    console.log(e.target.value);
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

    try {
      setIsLoading(true);
      const response = await fetch(`${API_URL}${endpoint}`, {
        method: "POST",
        body: formData,
      });
      const json = await response.json();
      setIsLoading(false);

      setResponseMessage(json["message"]);
      setUrl(json["url"]);
      setHexKey(json["key"])

      setShowResult(true);
      
      console.log("upload resp", json);
    } catch (error) {
      setIsLoading(false);
      setError(JSON.stringify(error));
      setShowResult(true);
    }
  };

  return (
    <>
      {showResult && <Result setShowResult={setShowResult} hexKey={hexKey} error={error} url={url} responseMessage={responseMessage} />}
      {!showResult && (
        <div>
          <h1>Image Upload</h1>
          {/* File input for image */}
          <input type="file" accept="image/*" onChange={handleImageChange} />

          {/* Image preview */}
          {preview && (
            <img
              src={preview}
              alt="Image preview"
              style={{ width: "200px", height: "auto" }}
            />
          )}
          {isDecryption && <input onChange={handleInputChange} />}

          {/* Button to upload image */}
          {image && (
            <button onClick={handleImageEncryption}>Upload Image</button>
          )}

          {isLoading && <Spinner />}
        </div>
      )}
    </>
  );
};

export default ImageUpload;
