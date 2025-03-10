import React, { useState } from "react";
import { Tabs } from "@mui/material";

import Tab from "@mui/material/Tab";
import ImageUpload from "./Components/ImageUpload.jsx";
import "./App.css";

const App = () => {
  const [tab, setTab] = useState("encryption");

  const changeTab = () => {
    if (tab === "encryption") {
      setTab("decryption");
    } else {
      setTab("encryption");
    }
  };


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
        {tab === "encryption" && <ImageUpload isDecryption={false} />}
        {tab === "decryption" && <ImageUpload isDecryption={true} />}
      </div>
    </div>
  );
};
export default App;
