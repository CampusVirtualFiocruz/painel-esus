import axios, { AxiosError, AxiosRequestConfig } from 'axios'
import { getUserLocalStorage } from '../context/AuthProvider/util';

export const Api = axios.create({
    // baseURL: "https://backend-ouropreto.painelsaude.info/v1/"
    baseURL: "http://demo.painelsaude.info:5001/v1/"
    // baseURL: "http://localhost:5001/v1/"
});

// Request interceptor
Api.interceptors.request.use(
    (config: AxiosRequestConfig) => {
        const user = getUserLocalStorage();

        config.headers = {
            Authorization: `Bearer ${user?.token}`
        };

        return config;
    },
    (error: AxiosError) => {
        console.log('AXIOS ERROR: ', error);
        return Promise.reject(error);
    }
);

// Response interceptor
Api.interceptors.response.use(
    (res) => {
        return res;
    },
    async (err: AxiosError) => {
        const originalConfig = err.config;

        if (originalConfig.url !== "auth" && err.response) {
            // Access Token was expired
            if (err.response.status === 401 && err.response.statusText === "UNAUTHORIZED") {
                localStorage.setItem("u", JSON.stringify(null));
                window.location.pathname = "/";
                return Promise.resolve();
            }
        }
        return Promise.reject(err);
    }
);
