import { Platform } from 'react-native';
import axios from 'axios'
import { API_SERVER_MOBILE, API_SERVER_WEB } from '@env'
import { getItemLocalStorage, removeItemLocalStorage } from './general-local-storage';

const axiosInstance = axios.create({
    baseURL: Platform.OS === 'web' ? API_SERVER_WEB : API_SERVER_MOBILE,
    timeout:10000,
    withCredentials: true,
    headers:{
        'Content-Type': 'application/json',
    },
});

// Configura el interceptor para añadir el token a las peticiones
axiosInstance.interceptors.request.use(
    async (config) => {
      //const token = Platform.OS === 'web' ? localStorage.getItem('userTokenLocalStorage') : await getItem('userToken');
      //console.log(token ? 'HAY TOKEN' : 'NO HAY TOKEN');
      //console.log(token);
      //console.log(await AsyncStorage.getItem('userToken'));
      //console.log(token);
      //console.log('BASEURL ' + Platform.OS === 'web' ? API_SERVER_WEB : API_SERVER_MOBILE);
      //removeItemLocalStorage('userToken');
      //removeItemLocalStorage('currentRoute');
      const token = await getItemLocalStorage('userToken');
      console.log(token);
      if (token) {
        config.headers.Authorization = `Token ${token}`;
      }
      return config;
    },
    (error) => {
      return Promise.reject(error);
    }
  );

export default axiosInstance;