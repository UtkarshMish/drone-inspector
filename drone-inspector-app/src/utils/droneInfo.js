import axios from "axios";

export async function getDroneInfo(pageNo) {
  try {
    const { data } = await axios.get(`/api/drones?page=${parseInt(pageNo)}`);

    if (data && data.result && data.total_pages) {
      const { result, total_pages } = data;
      return [result, total_pages];
    }
  } catch (error) {
    console.log(error);
  }
  return [[], 0];
}
