import { Box, Button } from "@chakra-ui/react";
import React from "react";
import { Link } from "react-router-dom";

export default function PageBox({ totalPage }) {
  const start_num = totalPage > 0 ? 1 : 0;
  const end_num = totalPage > 0 ? totalPage : 0;
  const BUTTON_LIST = [];
  if (end_num < 10) {
    for (let index = 1; index < end_num; index++) {
      BUTTON_LIST.push(
        <Button as={Link} to={`/view-data/${index}`}>
          {index}
        </Button>
      );
    }
  } else {
    BUTTON_LIST.push(
      <Button
        as={Link}
        to={`/view-data/${start_num}`}
        marginInline={"5"}
        variant={"solid"}
        colorScheme={"teal"}
      >
        {start_num}
      </Button>
    );
    BUTTON_LIST.push(
      <Button
        as={Link}
        to={`/view-data/${Math.floor(
          (parseInt(start_num) + parseInt(end_num)) / 2
        )}`}
        marginInline={"5"}
        variant={"solid"}
        colorScheme={"teal"}
      >
        {Math.floor((parseInt(start_num) + parseInt(end_num)) / 2)}
      </Button>
    );
    BUTTON_LIST.push(
      <Button
        as={Link}
        to={`/view-data/${end_num}`}
        marginInline={"5"}
        variant={"solid"}
        colorScheme={"teal"}
      >
        {end_num}
      </Button>
    );
  }

  return (
    <Box display={"flex"} justifyContent={"center"}>
      {BUTTON_LIST.map((item) => item)}
    </Box>
  );
}
