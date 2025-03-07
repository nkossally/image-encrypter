import React, { useState } from "react";
import { API_URL } from "../config";
import Spinner from "./Spinner";

const ImageUpload = ({ isDecryption, setError }) => {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [inputText, setInputText] = useState("");
  const [isLoading, setIsLoading] = useState(false)

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
    const formData = new FormData();
    formData.append("image", image);
    formData.append("key", inputText);

    const endpoint = isDecryption ? "/decrypt" : "/encrypt";

    try {
      setIsLoading(true)
      const response = await fetch(`${API_URL}${endpoint}`, {
        method: "POST",
        body: formData,
      });
      const json = await response.json();
      setIsLoading(false)

      console.log("upload resp", json);
    } catch (error) {
      setIsLoading(false)
      setError(JSON.stringify(error))
    }
  };

  return (
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
      {image && <button onClick={handleImageEncryption}>Upload Image</button>}

      {isLoading && <Spinner />}
    </div>
  );
};

export default ImageUpload;
