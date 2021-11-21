import { Box, Table, Tbody, Td, Text, Th, Thead, Tr } from "@chakra-ui/react";
import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getDroneInfo } from "../../utils/droneInfo";
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
      <Table>
        <Thead>
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
                  columns.map((val, inx) =>
                    typeof item[val] == "object" ? (
                      <ListValues item={item[val]} />
                    ) : (
                      <Td key={inx}>{item[val]}</Td>
                    )
                  )}
              </Tr>
            );
          })}
        </Tbody>
      </Table>
      <PageBox totalPage={totalPageCount} />
    </Box>
  ) : null;
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
          <Text fontWeight={"bold"}>{key}</Text>
          <Text>{value}</Text>
        </li>
      ))}
    </ul>
  );
}
