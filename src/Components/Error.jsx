import React, { useState } from "react";

const Error = ({ hideError, errorMessage }) => {
  const [image, setImage] = useState(null);

  const handleInputChange = (e) => {
    setInputText(e.target.value);
    console.log(e.target.value);
  };

  return <div></div>;
};

export default Error;
