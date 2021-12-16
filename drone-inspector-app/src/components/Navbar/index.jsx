import { Box, Button, Heading, Text } from "@chakra-ui/react";
import React from "react";
import { Link } from "react-router-dom";

export default function Navbar() {
	const MENU_LIST = [
		{ name: "View Data", link: "/view-data" },
		{ name: "Upload Data", link: "/upload-data" }
	];
	return (
		<Box
			display={"flex"}
			alignItems={"center"}
			justifyContent={"space-between"}
			paddingInline={"2"}
			w="100%">
			<Heading size={"md"}>
				<Text>Drone Application</Text>
			</Heading>
			<Box marginBlock={"2"}>
				{MENU_LIST &&
					Array.isArray(MENU_LIST) &&
					MENU_LIST.map(({ name, link }, indx) => (
						<Button
							marginInline={"2"}
							as={Link}
							to={link}
							key={indx}
							variant={"ghost"}
							_hover={{
								background: "transparent",
								boxShadow: "1px 1px 2px 2px #002988cf"
							}}
							_active={{ backgroundColor: "#122988cf", color: "white" }}>
							{name}
						</Button>
					))}
			</Box>
		</Box>
	);
}
