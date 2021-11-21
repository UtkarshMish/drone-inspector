import {
  Box,
  Button,
  Heading,
  Input,
  InputGroup,
  Text,
} from "@chakra-ui/react";
import React from "react";

export default function UploadBox() {
  return (
    <Box w="100%">
      <Heading size="xs">
        <Text>Upload Your Json</Text>
      </Heading>
      <form
        method="POST"
        action="/api/upload-data"
        encType="multipart/form-data"
      >
        <InputGroup
          display={"flex"}
          justifyContent={"space-around"}
          alignItems={"center"}
          paddingBlock={"10"}
        >
          <Text fontWeight={"semibold"}>Enter your file: </Text>
          <Input
            type={"file"}
            required
            maxWidth={"50%"}
            accept=".json"
            name="json_file"
          />
        </InputGroup>
        <Button type={"submit"} variant={"solid"} colorScheme={"green"}>
          Upload
        </Button>
      </form>
    </Box>
  );
}
