import React from "react";

const Error = ({ error, setError }) => {
  return (
    <div>
      <button onClick={()=>setError("")}>Back</button>

      {error}
    </div>
  );
};

export default Error;
