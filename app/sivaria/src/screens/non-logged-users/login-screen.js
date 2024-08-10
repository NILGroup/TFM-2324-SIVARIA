import { View, Platform, Text, useWindowDimensions, ScrollView } from 'react-native';
import React, { useContext, useEffect, useState } from 'react';
import ShowHidePasswordInput from '../../components/show-hide-password-input';

import axiosInstance from '../../utils/axios-config-web';
import stylesSivaria from '../../styles/styles-sivaria';
import { setItemLocalStorage } from '../../utils/general-local-storage';//import CookieManager from '@react-native-cookies/cookies';

import { usePushNotifications } from '../../utils/use-push-notifications';
import ModalComponent from '../../components/modal-component';
import SivariaText from '../../components/sivaria-text';
import SivariaButton from '../../components/sivaria-button';
import SivariaInput from '../../components/sivaria-input';

import Container from '../../components/component-containers/container';
import { AuthContext } from '../../context/auth-context';
import { UserContext } from '../../context/user-context';

import LoadingScreen from '../loading-screen';

import useModal from '../../utils/modal-hook';
//import { toast } from 'react-toastify';

//import Toast from 'react-native-toast-message';
import { useToast } from 'react-native-toast-notifications';

import { API_SERVER_MOBILE, API_SERVER_WEB } from '@env'


const LoginScreen = ({navigation}) => {

    const {expoPushToken, notification} = usePushNotifications();
    //const data = JSON.stringify(notification, undefined, 2);
    const toast = useToast();

    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const userApp = useContext(UserContext);
    const user = useContext(AuthContext);

    const { width, height } = useWindowDimensions();
    
    const { modalType, modalTitle, modalMessage, isVisible, setModalVisible, setVisibleModal } = useModal();

    const [isLoading, setIsLoading] = useState(false);

    const [isDisabled, setIsDisabled] = useState(true);

    async function callLogin(e) {
        //e.preventDefault();
        let message = '';

        if(!email) {
            message += 'El campo del email está vacío.\n\n';

        }
        if(!password) {            
            message += 'El campo de la contraseña está vacío.';

        }
        if(message.length !== 0) {
            toast.show(
                message,
                {
                    type:'danger'
                }
            );
        }
        else {
            setIsLoading(true);
            const data = {
                email:email,
                password:password,
            }

            if (Platform.OS !== 'web') {
                data['expo_token'] = expoPushToken.data
            }
            
            await axiosInstance.post('/sivaria/v1/user/login', data)
            .then(async function (response) {
                userData = response.data.data;  
                // Update local storage (web and mobile).
                await setItemLocalStorage('userToken', response.data.token);   
                await setItemLocalStorage('email', userData.email);  
                await setItemLocalStorage('userId', userData.id);  
                await setItemLocalStorage('firstName', userData.first_name);  
                await setItemLocalStorage('lastName', userData.last_name);  
                await setItemLocalStorage('phoneNumber', userData.phone);  
                let rolDescription = (userData.rol) ? userData.rol.description : null;
                await setItemLocalStorage('rol', rolDescription);  
                let rolSlug = (userData.rol) ? userData.rol.slug : null;
                await setItemLocalStorage('rolSlug', rolSlug); 
                if(rolSlug === 'joven') {
                    await setItemLocalStorage('emailParent1', userData.email_parent_1 ?? ''); 
                    await setItemLocalStorage('emailParent2', userData.email_parent_2 ?? ''); 
                }
                // Updating state of the user data
                userApp.setUserId(userData.id);
                userApp.setFirstName(userData.first_name ?? '');
                userApp.setLastName(userData.last_name?? '');
                userApp.setEmail(userData.email ?? '');
                userApp.setPhoneNumber(userData.phone ?? '');
                userApp.setRol(rolDescription);
                userApp.setRolSlug(rolSlug);
                if(rolSlug === 'joven') {
                    userApp.setEmailParent1(userData.email_parent_1 ?? '');
                    userApp.setEmailParent2(userData.email_parent_2 ?? '');
                }
                
                //userApp.insertUserData(userData);

                //toast.success('Usuario logeado exitosamente');
                toast.show(
                    'Usuario logeado exitosamente',
                    {
                        type: 'success'
                    }
                );
                //console.log('CAMBIANDO EL AUTENTICATED');
                //console.log(user.isAuthenticated);
                //user.login(); 
                //console.log(user.isAuthenticated);
                user.setIsAuthenticated(true);
            })
            .catch(function (error) {
                toast.show(
                    'Error durante el proceso de login. ' + error.response.data.data,
                    {
                        type: 'danger'
                    }
                );
            });
            setIsLoading(false);
        }
    }


    useEffect(() => {
        function enableLoginButton(){
            if(email && password) {
                setIsDisabled(false);
            }
            else {
                setIsDisabled(true);
            }
        }
        enableLoginButton();
    }, [email, password]);

    if (isLoading) {
        return (
            <LoadingScreen />
        );
    }
    return (
        <ScrollView>
            <ModalComponent 
                animationType='slide'
                setIsVisible={setModalVisible}
                isVisible={isVisible}
                title={modalTitle}
                modalType={modalType}
                message={modalMessage}
            />
            <View style={{height: 200, alignItems: 'center', justifyContent: 'center', backgroundColor: '#006E51'}}>
                <Text onPress={(e) => navigation.navigate('Login')} style={{color:'white', fontSize: 35, fontWeight: 'bold', textAlign: 'center'}}>SIVARIA</Text>
            </View>

            <View style={{height: 500, backgroundColor: '#006E51', alignItems: 'center', justifyContent: 'center'}} >

                <View style={stylesSivaria.whiteBoxContainer}>

                    <View style={{height:100, alignItems:'center', justifyContent: 'center'}}>
                        <SivariaInput
                            placeholder={'Email'}
                            value={email}
                            onChangeText={setEmail}
                            autoCorrect={false}
                            autoCapitalize={'none'}
                            inputMode={'email'}
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
                            {/*<SivariaText color={'#006E51'}>¿Olvidaste tu contraseña?</SivariaText>*/}
                            <Text onPress={(e) => navigation.navigate('ForgotPassword')} style={{color:'#006E51', fontSize:15}}>
                                ¿Olvidaste tu contraseña?
                            </Text>
                            {/*<a id='forgot_password_link' onClick={navigation.navigate('ForgotPassword')} href="#">Click here</a>*/}
                        </View>
                    </View>

                    <View style={{height:80, alignItems:'center', justifyContent: 'center'}}>
                        <SivariaButton onPress={(e) => callLogin(e)} message={'INICIAR SESIÓN'} disabled={isDisabled}/>
                    </View>

                    <View style={{height:80, alignItems:'center', justifyContent: 'center'}}>
                        <SivariaButton onPress={() => navigation.navigate('Register')} message={'REGISTRARSE'} />
                    </View>
                </View>
            </View>

            <View style={{height:80, alignItems:'center', justifyContent: 'center', backgroundColor: '#006E51'}} >
                <SivariaText color={'white'} isBold={false}>Hecho por Aldair Maldonado</SivariaText>   
            </View>
        </ScrollView>
    );
    /*
        Meter para probar si se crea un Expo Token
        <Text>Token: {expoPushToken?.data ?? ""}</Text>
        <Text>{data}</Text>
    */
}

export default LoginScreen;