import { Box } from "@chakra-ui/react";
import "./App.css";
import Layout from "./components/Layout/Layout";

function App() {
	return (
		<Box className="App" maxH={"100vh"} overflow={"auto"}>
			<Layout />
		</Box>
	);
}

export default App;
