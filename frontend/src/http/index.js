import axios from "axios";

const baseURL = import.meta.env.VITE_API_BASE_URL;

const apiClient = axios.create({
  baseURL: baseURL,
  withCredentials: true,
  headers: {
    Accept: "application/json",
    "Content-type": "application/json",
  },
});

export default apiClient;
