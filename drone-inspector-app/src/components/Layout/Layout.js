import { Box } from "@chakra-ui/react";
import React, { useEffect, useRef } from "react";
import { BrowserRouter as Router } from "react-router-dom";
import MainContent from "../MainContent";

import Map from "../Map/Map";
import MapService, { MAPBOX_ACCESS_TOKEN } from "../Map/MapService";

import "./Layout.css";

export default function Layout() {
  const mapService = useRef(null);

  useEffect(() => {
    // initialize only once
    if (mapService.current) {
      return;
    }
    const mapObj = new MapService();
    mapObj.initMap();
    mapService.current = mapObj;
  }, []);

  return (
    <Box
      display={"flex"}
      justifyContent={"space-between"}
      borderRadius={"base"}
    >
      <Router>
        <MainContent />
      </Router>
      <Box className="layout__map_cont">{MAPBOX_ACCESS_TOKEN && <Map />}</Box>
    </Box>
  );
}
