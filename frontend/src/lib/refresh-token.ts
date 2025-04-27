import axios from "axios";

const refreshToken = async (): Promise<string | null> => {
  try {
    const refresh = localStorage.getItem("refreshToken");
    if (!refresh) {
      console.error("No refresh token found");
      return null;
    }

    const response = await axios.post(
      "http://localhost:8000/api/token/refresh/",
      {
        refresh,
      }
    );

    localStorage.setItem("accessToken", response.data.access);
    return response.data.access;
  } catch (error) {
    console.error("Error refreshing token:", error);
    return null;
  }
};

export default refreshToken;
