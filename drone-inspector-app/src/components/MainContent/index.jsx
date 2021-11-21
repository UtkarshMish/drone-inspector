import { Box } from "@chakra-ui/react";
import React from "react";
import { Route, Routes } from "react-router-dom";
import UploadBox from "../common/UploadBox";
import ViewTable from "../common/ViewTable";
import Navbar from "../Navbar";

export default function MainContent() {
  return (
    <Box width={"50%"} maxH={"inherit"}>
      <Navbar />
      <Box maxHeight="92vh" overflow={"auto"}>
        <Routes>
          <Route path="/view-data/" element={<ViewTable />} />
          <Route path="/view-data/:page" element={<ViewTable />} />
          <Route path="/upload-data" element={<UploadBox />} />
          <Route path="/" element={<ViewTable />} />
        </Routes>
      </Box>
    </Box>
  );
}
