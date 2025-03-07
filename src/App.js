import React, { useState } from "react";
import { Tabs } from "@mui/material";

import Tab from "@mui/material/Tab";
import ImageUpload from "./Components/ImageUpload.jsx";
import Spinner from "./Components/Spinner.js";
import Error from "./Components/Error.jsx";
import "./App.css";

const App = () => {
  const [tab, setTab] = useState("encryption");
  const [error, setError] = useState("")
  const [isLoading, setIsLoading] = useState(false)


  const changeTab = () => {
    if (tab === "encryption") {
      setTab("decryption");
    } else {
      setTab("encryption");
    }
  };

  if(error){
    return(
      <Error error={error} setError={setError} />
    )
  }

  return (
    <div className="container">
      <Tabs
        value={tab}
        onChange={changeTab}
        aria-label="wrapped label tabs example"
      >
        <Tab
          value="encryption" label="encryption"
        />
        <Tab value="decryption" label="decryption" />
      </Tabs>
      <div>
        {tab === "encryption" && <ImageUpload isDecryption={false} setError={setError} />}
        {tab === "decryption" && <ImageUpload isDecryption={true} setError={setError} />}
      </div>
    </div>
  );
};
export default App;
