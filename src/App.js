import React, { useState } from "react";
import { Tab } from '@mui/material';
import { TabList, TabContext, TabPanel } from '@mui/lab';


import { Info } from "./Components/Info.jsx";
import ImageUpload from "./Components/ImageUpload.jsx";
import "./index.css";

const App = () => {
  const [tab, setTab] = useState("encryption");

  const handleChange = (event, newValue) => {
    setTab(newValue);
  };

  return (
    <div className="container">
      <TabContext value={tab}>
        <TabList onChange={handleChange} aria-label="lab API tabs example">
          <Tab value="encryption" label="Encrypt" />
          <Tab value="decryption" label="Decrypt" />
          <Tab value="info" label="Info" />
        </TabList>
        <TabPanel value="encryption">
          <ImageUpload isDecryption={false} />
        </TabPanel>
        <TabPanel value="decryption">
          <ImageUpload isDecryption={true} />
        </TabPanel>
        <TabPanel value="info">
          <Info />
        </TabPanel>
      </TabContext>
    </div>
  );
};
export default App;
