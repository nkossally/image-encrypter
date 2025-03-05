import React, { useState } from 'react';
import { API_URL } from '../config'

const ImageUpload = () => {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setImage(file);
      setPreview(URL.createObjectURL(file)); // Generate preview URL for image
    }
  };

  const handleImageUpload = async () => {
    const formData = new FormData();
    formData.append("image", image);
    console.log(image)

    try {
      const response = await fetch(`${API_URL}/upload`, {
        method: "POST",
        body: formData,
      });
      const json = await response.json();
      console.log("upload resp", json); 
    } catch (error) {
      console.error("Error:", error);
      alert("Error uploading image");
    }
  };

  return (
    <div>
      <h1>Image Upload</h1>
      {/* File input for image */}
      <input type="file" accept="image/*" onChange={handleImageChange} />
      
      {/* Image preview */}
      {preview && <img src={preview} alt="Image preview" style={{ width: '200px', height: 'auto' }} />}
      
      {/* Button to upload image */}
      {image && <button onClick={handleImageUpload}>Upload Image</button>}
    </div>
  );
};

export default ImageUpload;
