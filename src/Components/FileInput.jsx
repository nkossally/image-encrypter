import { useRef } from 'react';         
import "../index.css";

export const FileInput = ({handleImageChange}) => { // REVISED
  const hiddenFileInput = useRef(null); 

  const handleClick = event => {
    hiddenFileInput.current.click();   
  };

  const handleChange = event => {
    const fileUploaded = event.target.files[0];
    handleImageChange(fileUploaded);                   // ADDED
  };

  return (
    <>
      <button 
        className="file-input"
        onClick={handleClick}
      >
        Choose a file
      </button>
      <input 
        type="file"
        onChange={handleChange}
        ref={hiddenFileInput}
        style={{display:'none'}}
      />
    </>
  );
};

export default FileInput;
