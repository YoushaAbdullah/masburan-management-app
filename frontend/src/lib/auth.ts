import axios from "axios";

export const refreshToken = async () => {
  try {
    const refresh = localStorage.getItem("refreshToken");
    const res = await axios.post("/api/token/refresh/", { refresh });
    if (res.status === 200) {
      localStorage.setItem("accessToken", res.data.access);
      return res.data.access;
    }
  } catch (err) {
    console.error("Refresh failed:", err);
    return null;
  }
};
