import { Box, Button } from "@chakra-ui/react";
import React from "react";
import { Link } from "react-router-dom";

export default function PageBox({ totalPage, currentNum }) {
  const start_num = totalPage > 0 ? 1 : 0;
  const end_num = totalPage > 0 ? parseInt(totalPage) - 1 : 0;
  const BUTTON_LIST = [];
  if (end_num < 10) {
    for (let index = 1; index < end_num; index++) {
      BUTTON_LIST.push(
        <Button as={Link} to={`/view-data/${index}`} key={index} margin={5}>
          {index}
        </Button>
      );
    }
  } else {
    const page_list = [
      start_num,
      parseInt(currentNum),
      Math.ceil((start_num + end_num) / 2),
      end_num,
    ];
    if (currentNum > 1) {
      page_list.push(currentNum - 1);
    }
    if (currentNum < end_num) {
      page_list.push(currentNum + 1);
    }
    new Set(page_list.sort((a, b) => a - b)).forEach((value, key) =>
      BUTTON_LIST.push(
        <Button
          as={Link}
          to={`/view-data/${value}`}
          key={key + value}
          margin={5}
        >
          {value}
        </Button>
      )
    );
  }

  return (
    <Box display={"flex"} justifyContent={"center"}>
      {BUTTON_LIST}
    </Box>
  );
}
