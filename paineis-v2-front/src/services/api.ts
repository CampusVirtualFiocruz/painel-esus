import axios, { AxiosError, AxiosRequestConfig } from 'axios';
import { getUserLocalStorage } from '../context/AuthProvider/util';

const URL = window.location.host;
const PROTOCOL = window.location.protocol;

const get_url_env = () => {
  let isProd = true;

  if (parseInt(window.location.port) === 3000) {
    isProd = false;
  } else if (process.env.hasOwnProperty('REACT_APP_ENV')) {
    isProd = process.env.REACT_APP_ENV?.indexOf('dev') === -1;
  } else if (process.env.hasOwnProperty('REACT_APP_NODE_ENV')) {
    isProd = process.env.REACT_APP_NODE_ENV?.indexOf('dev') === -1;
  }
  return isProd ? `${PROTOCOL}//${URL}/v1/` : 'http://localhost:5001/v1/';
};
const API_URL = get_url_env();

export const Api = axios.create({
  baseURL: API_URL,
});

// Request interceptor
Api.interceptors.request.use(
  (config: AxiosRequestConfig) => {
    const user = getUserLocalStorage();

    config.headers = {
      Authorization: `Bearer ${user?.token}`,
    };

    return config;
  },
  (error: AxiosError) => {
    console.error('AXIOS ERROR: ', error);
    return Promise.reject(error);
  }
);

// Response interceptor
Api.interceptors.response.use(
  res => {
    return res;
  },
  async (err: AxiosError) => {
    const originalConfig = err.config;

    if (originalConfig.url !== 'auth' && err.response) {
      // Access Token was expired
      if (
        err.response.status === 401 &&
        err.response.statusText === 'UNAUTHORIZED'
      ) {
        localStorage.setItem('u', JSON.stringify(null));
        window.location.pathname = '/';
        return Promise.resolve();
      }
    }
    return Promise.reject(err);
  }
);
