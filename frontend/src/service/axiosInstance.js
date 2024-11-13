import axios from "axios";

// Ainda será implementado o token jwt no login e cadastro de admin

//export const BASE_URL = "http://localhost:8080"
export const BASE_URL = "https://api-tcc-j7s2.onrender.com"

export const axiosInstance = axios.create({
    baseURL: BASE_URL,
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
});
