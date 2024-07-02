//import axios from 'axios';
import { ScrollView, StyleSheet, Alert, Text, TextInput, View, SafeAreaView, Pressable, Platform, NativeModules, useWindowDimensions } from 'react-native';
import React, { useContext, useState } from 'react';
import { useNavigation } from '@react-navigation/native';
import axios from 'axios';
import ShowHidePasswordInput from '../components/show-hide-password-input';

import { API_SERVER } from '@env'

//import { Container } from 'react-bootstrap';
import Navbar from 'react-bootstrap';
import Button from 'react-bootstrap';
import { Form } from 'react-bootstrap';

import axiosInstance from '../utils/axios-config-web';
import stylesSivaria from '../styles/styles-sivaria';
import { setItemLocalStorage, removeItemLocalStorage, getItemLocalStorage } from '../utils/general-local-storage';//import CookieManager from '@react-native-cookies/cookies';

import { usePushNotifications } from '../utils/use-push-notifications';
import ModalComponent from '../components/modal-component';
import SivariaText from '../components/sivaria-custom-basic-components/sivaria-text';
import SivariaButton from '../components/sivaria-custom-basic-components/sivaria-button';
import SivariaButtonContainer from '../components/component-containers/sivaria-button-container';
import SivariaInput from '../components/sivaria-custom-basic-components/sivaria-input';

import Container from '../components/component-containers/container';
import { ModalType, ModalTitle } from '../utils/enum-types-modal';
import { AuthContext } from '../context/auth-context';
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

const LoginScreen = ({navigation}) => {

    const {expoPushToken, notification} = usePushNotifications();
    const data = JSON.stringify(notification, undefined, 2);
    //console.log('Data '+data);

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const { setIsAuthenticated } = useContext(AuthContext);

    const { width, height } = useWindowDimensions();
    
    const [modalType, setModalType] = useState('');
    const [modalTitle, setModalTitle] = useState('');
    const [modalMessage, setModalMessage] = useState('');
    const [isVisible, setModalVisible] = useState(false);

    function setVisibleModal(modalType, title, message) {
        setModalType(modalType)
        setModalTitle(title);
        setModalMessage(message);
        setModalVisible(true);
    }

    async function callLogin(e) {
        e.preventDefault();
        let message = '';

        if(!email) {
            message += 'El campo del email está vacío.\n\n';

        }
        if(!password) {            
            message += 'El campo de la contraseña está vacío.\n\n';

        }
        if(message.length !== 0) {
            setVisibleModal(ModalType.Error, ModalTitle.ErrorTitle, message);
        }
        else {

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
                    userData = response.data.data;  
                    console.log(response.data.token);    
                    await setItemLocalStorage('userToken', response.data.token);   
                    await setItemLocalStorage('email', userData.email);
                    /*
                    console.log('HOLA');
                    console.log(response);
                    console.log(response.data);
                    console.log(response.data.data);
                    console.log(response.data.token);
                    userData = response.data.data;
                    setItemLocalStorage('userToken', response.data.token);
                    let userDataArray = {
                        email: userData.email,
                        firstName: userData.first_name ?? null,
                        lastName: userData.last_name ?? null,
                        phone: userData.phone ?? null,
                        rolDescription: userData.rol.description ?? null,
                        rolSlug: userData.rol.slug ?? null,
                    }
                    console.log(userDataArray)
                    if ('email_parent_1' in userDataArray) {
                        userDataArray['emailParent1'] = userData.email_parent_1 ?? null;
                    }
                    if ('email_parent_2' in userDataArray) {
                        userDataArray['emailParent2'] = userData.email_parent_2 ?? null;
                    }
                    console.log('HOLA 2');
                    setItemLocalStorage('firstName', userData.first_name ?? null);
                    setItemLocalStorage('lastName', userData.last_name ?? null);
                    setItemLocalStorage('phone', userData.phone ?? null);
                    setItemLocalStorage('rol', userData.rol.description ?? null);
                    setItemLocalStorage('rolSlug', userData.rol.slug ?? null);
                    if ('email_parent_1' in userData) {
                        setItemLocalStorage('emailParent1', userData.email_parent_1 ?? null);
                    }
                    if ('email_parent_1' in userData) {
                        setItemLocalStorage('emailParent2', userData.email_parent_2 ?? null);
                    }
                    console.log('HOLA 3');

                    setItemLocalStorage('userData', btoa(userDataArray));
                    */
                    //setItemLocalStorage('emailParent1', userData.email_parent_1);
                    //setItemLocalStorage('emailParent2', userData.email_parent_2);
                    
                    //axiosInstance.defaults.withCredentials = true;
                    //axiosInstance.defaults.xsrfHeaderName = "X-CSRFTOKEN";
                    //axiosInstance.defaults.xsrfCookieName = "csrftoken";
                    
                    //axiosInstance.defaults.xsrfHeaderName = response.config.xsrfHeaderName;
                    //axiosInstance.defaults.xsrfCookieName = response.config.xsrfCookieName;
                    
                    //console.log(getItemLocalStorage('userToken'));

                    // Navegar a la siguiente pantalla (Home, por ejemplo)
                    //console.log('Login exitoso');
                    setIsAuthenticated(true); 
                    //navigation.navigate('Home');
                    //navigation.navigate('Root', {screen: 'Home'});
                })
                .catch(function (error) {
                    //setModalType(ModalType.Error)
                    //setModalTitle(ModalTitle.ErrorTitle);
                    
                    //const message = <SivariaText fontSize={20} color={'black'}>Ha habido un error durante el proceso de login.</SivariaText>
                    //message += <SivariaText fontSize={20} color={'black'}>{error.response.data.data}</SivariaText>
                    
                    const message = 'Ha habido un error durante el proceso de login. ' + error.response.data.data;
                    //setModalVisible(true);
                    setVisibleModal(ModalType.Error, ModalTitle.ErrorTitle, message)
                    //console.error('Error de inicio de sesión:', error);
                    //Alert.alert('Error', 'Error en el inicio de sesión. Inténtelo de nuevo.')
                });
            }
    }

    return (
        <Container>
            <ModalComponent 
                animationType='slide'
                setIsVisible={setModalVisible}
                isVisible={isVisible}
                title={modalTitle}
                modalType={modalType}
                message={modalMessage}
            />
            <View style={{height: 200, alignItems: 'center', justifyContent: 'center'}}>
                <SivariaText isBold={true} fontSize={35}>SIVARIA</SivariaText>
            </View>

            <View style={{flex:3, backgroundColor: '#006E51', alignItems: 'center', justifyContent: 'center'}} >

                <View style={stylesSivaria.whiteBoxContainer}>

                    <View style={{height:100, alignItems:'center', justifyContent: 'center'}}>
                        <SivariaInput
                            placeholder={'Email'}
                            value={email}
                            onChangeText={setEmail}
                            autoCorrect={false}
                            autoCapitalize={'none'}
                        />       
                    </View>

                    <View style={{height:100, alignItems:'center', justifyContent: 'center'}}>
                        <ShowHidePasswordInput
                            placeholder='Contraseña' 
                            password={password} 
                            onChangeText={setPassword} />
                    </View>

                    <View style={{height:40, alignItems:'center', justifyContent: 'center'}}>
                        <View style={{width:'80%', alignItems: 'flex-end', justifyContent: 'center'}}>
                            <SivariaText color={'#006E51'}>¿Olvidaste tu contraseña?</SivariaText>
                        </View>
                    </View>

                    <View style={{height:80, alignItems:'center', justifyContent: 'center'}}>
                        <SivariaButton onPress={(e) => callLogin(e)}>
                            <SivariaText color={'white'} isBold={true}>
                                INICIAR SESIÓN
                            </SivariaText>
                        </SivariaButton>
                    </View>

                    <View style={{height:80, alignItems:'center', justifyContent: 'center'}}>
                        <SivariaButton onPress={() => navigation.navigate('Register')}>
                            <SivariaText isBold={true}>
                                REGISTRARSE
                            </SivariaText>
                        </SivariaButton>
                    </View>
                </View>
            </View>

            <View style={{height:80, alignItems:'center', justifyContent: 'center'}} >
                <SivariaText color={'white'} isBold={false}>Hecho por Aldair Maldonado</SivariaText>   
            </View>
        </Container>
    );
    /*
        Meter para probar si se crea un Expo Token
        <Text>Token: {expoPushToken?.data ?? ""}</Text>
        <Text>{data}</Text>
    */
}

export default LoginScreen;