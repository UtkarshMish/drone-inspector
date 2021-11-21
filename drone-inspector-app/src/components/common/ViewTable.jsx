import { Box, Table, Tbody, Td, Text, Th, Thead, Tr } from "@chakra-ui/react";
import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getDroneInfo } from "../../utils/droneInfo";
import { Spinner } from "@chakra-ui/spinner";
import PageBox from "./PageBox";

export default function ViewTable() {
  const [droneData, setDroneData] = useState(null);
  const [columns, setColumns] = useState(null);
  const { page } = useParams() || { page: 1 };
  const [totalPageCount, setTotalPageCount] = useState(1);
  useEffect(() => {
    async function setDroneFromAPI() {
      const [data, pages] = await getDroneInfo(page);
      if (data && Array.isArray(data)) {
        setDroneData(data);
        setTotalPageCount(pages);
        if (data.length > 1) {
          setColumns(Object.keys(data[0]));
        }
      }
    }

    return setDroneFromAPI();
  }, [page]);
  return droneData && Array.isArray(droneData) ? (
    <Box display={"flex"} flexDirection={"column"}>
      <Table variant="striped" colorScheme="cyan">
        <Thead bgColor={"cyan"}>
          <Tr>
            {columns &&
              Array.isArray(columns) &&
              columns.map((item, key) => <Th key={key}>{item}</Th>)}
          </Tr>
        </Thead>
        <Tbody>
          {droneData.map((item, keyValue) => {
            return (
              <Tr key={keyValue}>
                {columns &&
                  Array.isArray(columns) &&
                  columns.map((val, inx) => (
                    <Td key={inx}>
                      <Box width="12rem" height="6rem" overflow="auto">
                        {typeof item[val] === "object" ? (
                          <ListValues item={item[val]} />
                        ) : ["phone", "_id", "reg_id"].includes(
                            val.toLowerCase()
                          ) || isNaN(parseFloat(item[val])) ? (
                          item[val]
                        ) : (
                          parseFloat(item[val]).toFixed(2)
                        )}
                      </Box>
                    </Td>
                  ))}
              </Tr>
            );
          })}
        </Tbody>
      </Table>
      <PageBox totalPage={totalPageCount} currentNum={parseInt(page)} />
    </Box>
  ) : (
    <Spinner size="lg" thickness="4px" speed="0.65s" />
  );
}

function ListValues({ item }) {
  return (
    <ul>
      {Object.entries(item).map(([key, value], inx) => (
        <li
          key={inx}
          style={{
            display: "flex",
            justifyContent: "space-between",
            paddingInline: "10px",
            marginBlock: "10px",
          }}
        >
          <Text fontWeight={"bold"} maxWidth={"50%"}>
            {key}
          </Text>
          <Text maxWidth={"50%"}>
            {["phone", "_id", "address"].includes(key.toLowerCase()) ||
            isNaN(parseFloat(value))
              ? value
              : parseFloat(value).toFixed(2)}
          </Text>
        </li>
      ))}
    </ul>
  );
}
