import axios from 'axios'
import { API_SERVER } from '@env'
//import CookieManager from '@react-native-cookies/cookies';

const axiosInstance = axios.create({
    baseURL: API_SERVER,
    timeout:10000,
    headers:{
        'Content-Type': 'application/json'
    },
    withCredentials: true,
});
/*
axiosInstance.interceptors.request.use(
    async (config) => {
      // Añadir cookies a la petición si withCredentials es true
      const cookies = await CookieManager.get(API_SERVER);
      config.headers.Cookie = Object.entries(cookies)
        .map(([name, cookie]) => `${name}=${cookie.value}`)
        .join('; ');
      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
  );
  
axiosInstance.interceptors.response.use(
    async (response) => {
      // Almacenar cookies recibidas en el cliente
      const setCookieHeader = response.headers['set-cookie'];
      if (setCookieHeader) {
        setCookieHeader.forEach((cookie) => {
          const [cookieName, cookieValue] = cookie.split(';')[0].split('=');
          CookieManager.set(API_SERVER, {
            name: cookieName,
            value: cookieValue,
            domain: '127.0.0.1',
            path: '/',
          });
        });
      }
      return response;
    },
    (error) => {
      return Promise.reject(error);
    }
  );
*/
export default axiosInstance;