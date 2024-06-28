//import axios from 'axios';
import { ScrollView, StyleSheet, Alert, Text, TextInput, View, SafeAreaView, Pressable, Platform, NativeModules, useWindowDimensions } from 'react-native';
import React, { useState } from 'react';
import { useNavigation } from '@react-navigation/native';
import axios from 'axios';
import ShowHidePasswordInput from '../components/show-hide-password-input';

import { API_SERVER } from '@env'

import { Container } from 'react-bootstrap';
import Navbar from 'react-bootstrap';
import Button from 'react-bootstrap';
import { Form } from 'react-bootstrap';

import axiosInstance from '../utils/axios-config-web';
import stylesSivaria from '../styles/styles-sivaria';
import { setItemLocalStorage, removeItemLocalStorage, getItemLocalStorage } from '../utils/general-local-storage';//import CookieManager from '@react-native-cookies/cookies';

import { usePushNotifications } from '../utils/use-push-notifications';

/*
let axiosInstance;
if (Platform.OS !== 'web') {
    axiosInstance = require('../components/axios-config-mobile').default;
}
else {
    axiosInstance = require('../components/axios-config-web').default;
}
    */

const { StatusBarManager } = NativeModules;
//axiosInstance.defaults.xsrfCookieName = 'csrftoken';
//axiosInstance.defaults.xsrfHeaderName = 'X-XSRFToken';
//axiosInstance.defaults.withCredentials = true;

const LoginScreen = ({navigation, route}) => {

    const {expoPushToken, notification} = usePushNotifications();
    const data = JSON.stringify(notification, undefined, 2);
    //console.log('Data '+data);

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const { setIsAuthenticated } = route.params;

    const windowDimensions = useWindowDimensions();

    async function callLogin(e) {
        e.preventDefault();

        if(!email && !password) {
            Alert.alert('Error', 'El campo email y contraseña están vacíos.')
        }

        if(!email) {
            Alert.alert('Error', 'El campo email está vacío.')
        }

        if(!password) {            
            Alert.alert('Error', 'El campo contraseña está vacío.')
        }

        const data = {
            email:email,
            password:password,
        }

        if (Platform.OS !== 'web') {
            data['expo_token'] = expoPushToken.data
        }

        await axiosInstance.post('/sivaria/v1/user/login', data)
            .then(async function (response) {
                //const token = response.data.data.token;
                //console.log('Token JWT:', token);
                
                // Llamar función para resetear campos después del login exitoso
                //setEmail('');
                //setPassword('');
                //console.log(response);

                /*
                if(Platform.OS !== 'web') {
                    const setCookieHeader = response.headers['set-cookie'];
                    if(setCookieHeader) {
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
                }
                */
               //console.log(response.data);
               //console.log(response.data.token);
                userData = response.data.data;
                setItemLocalStorage('userToken', response.data.token);
                setItemLocalStorage('email', userData.email);

                //axiosInstance.defaults.withCredentials = true;
                //axiosInstance.defaults.xsrfHeaderName = "X-CSRFTOKEN";
                //axiosInstance.defaults.xsrfCookieName = "csrftoken";
                
                //axiosInstance.defaults.xsrfHeaderName = response.config.xsrfHeaderName;
                //axiosInstance.defaults.xsrfCookieName = response.config.xsrfCookieName;
                
                //console.log(getItemLocalStorage('userToken'));

                // Navegar a la siguiente pantalla (Home, por ejemplo)
                console.log('Login exitoso');
                setIsAuthenticated(true); 
                //navigation.navigate('Home');
                //navigation.navigate('Root', {screen: 'Home'});
                
            })
            .catch(function (error) {
                console.error('Error de inicio de sesión:', error);
                Alert.alert('Error', 'Error en el inicio de sesión. Inténtelo de nuevo.')
            });
    }

    return (
        <SafeAreaView style={stylesSivaria.container}>
            <View style={stylesSivaria.header}>
                <Text style={stylesSivaria.title}>SIVARIA</Text>
            </View>
            <View style={stylesSivaria.formContainer}>
                <TextInput
                            style={stylesSivaria.input}
                            placeholder='Email'
                            placeholderTextColor={'#aaa'}
                            value={email} 
                            onChangeText={setEmail} 
                            autoCorrect={false}
                            autoCapitalize='none' />

                <ShowHidePasswordInput 
                        style={stylesSivaria.input}
                        placeholder='Contraseña' 
                        password={password} 
                        onChangeText={setPassword} />

                <Pressable 
                    style={stylesSivaria.button}
                    onPress={(e) => callLogin(e)}>
                    <Text style={stylesSivaria.buttonText} >Iniciar sesión</Text>
                </Pressable>

                <Pressable 
                    style={stylesSivaria.button}
                    onPress={() => navigation.navigate('Register')}>
                    <Text style={stylesSivaria.buttonText}>Registrarse</Text>
                </Pressable>

            </View>
            <View style={stylesSivaria.footer}>
                <Text style={stylesSivaria.buttonText}>Hecho por Aldair Maldonado</Text>
            </View>
            
        </SafeAreaView>
    );
    /*
        Meter para probar si se crea un Expo Token
        <Text>Token: {expoPushToken?.data ?? ""}</Text>
        <Text>{data}</Text>
    */
}

export default LoginScreen;