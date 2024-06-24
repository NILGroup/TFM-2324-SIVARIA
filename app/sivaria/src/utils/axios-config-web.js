import { Platform } from 'react-native';
import axios from 'axios'
import { API_SERVER_MOBILE, API_SERVER_WEB } from '@env'

const axiosInstance = axios.create({
    baseURL: Platform.OS === 'web' ? API_SERVER_WEB : API_SERVER_MOBILE,
    timeout:10000,
    withCredentials: true,
    headers:{
        'Content-Type': 'application/json',
    },
});

export default axiosInstance;