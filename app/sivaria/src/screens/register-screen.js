import React, { useEffect, useState } from 'react';
import { StyleSheet, ActivityIndicator, ScrollView, SafeAreaView, View, Text, TextInput, Pressable, Alert, Dimensions, Platform } from 'react-native';
import Dropdown from '../components/sivaria-custom-basic-components/dropdown';
import ShowHidePasswordInput from '../components/show-hide-password-input';
import axiosInstance from '../utils/axios-config-web';
import stylesSivaria from '../styles/styles-sivaria';
import PhoneInput from "react-native-phone-input";
import LoadingScreen from './loading-screen';

import SivariaText from '../components/sivaria-custom-basic-components/sivaria-text';
import SivariaInput from '../components/sivaria-custom-basic-components/sivaria-input';
import SivariaButton from '../components/sivaria-custom-basic-components/sivaria-button';
import Container from '../components/component-containers/container';

import ModalComponent from '../components/modal-component';

import { ModalType, ModalTitle } from '../utils/enum-types-modal';

import { usePushNotifications } from '../utils/use-push-notifications';

const { height } = Dimensions.get('window');

const RegisterScreen = ({navigation}) => {

    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [phoneNumber, setPhoneNumber] = useState('');
    const [rol, setRol] = useState('');
    const [emailParent1, setEmailParent1] = useState('');
    const [emailParent2, setEmailParent2] = useState('');

    const [roles, setRoles] = useState([]);

    const [loading, setLoading] = useState(true);


    const [showExtraText, setShowExtraText] = useState(false);

    const [modalType, setModalType] = useState('');
    const [modalTitle, setModalTitle] = useState('');
    const [modalMessage, setModalMessage] = useState('');
    const [isVisible, setModalVisible] = useState(false);

    
    const {expoPushToken, notification} = usePushNotifications();


    useEffect(() => {
        const fetchRoles = async () => {
            await axiosInstance.get('/sivaria/v1/rol')
            .then(function (response) {
                const rolesData = response.data.data.rols.map(role => ({
                    label: role.description, // Ajusta esto según la estructura de tu JSON
                    value: role.slug // Ajusta esto según la estructura de tu JSON
                }));
                setRoles(rolesData);
            })
            .catch(function (error) {
                let message = 'No se han podido cargar los roles de los usuarios.';
                setVisibleModal(ModalType.Error, ModalTitle.ErrorTitle, message)
            });

            setLoading(false);

        };
    
        fetchRoles();
      }, []
    );
      /*
    useEffect(() => {
        // AÑADIR VALIDACIONES
    }, [firstName, lastName, email, password, confirmPassword, phoneNumber, rol, phoneNumberParent1, phoneNumberParent2]);
*/

    function setVisibleModal(modalType, title, message) {
        setModalType(modalType)
        setModalTitle(title);
        setModalMessage(message);
        setModalVisible(true);
    }

    const handleSubmit = async () => {
        let message = '';
        if(!firstName) {
            message += 'El campo del nombre está vacío.\n\n';
        }
        if(!lastName) {
            message += 'El campo de los apellidos está vacío.\n\n';
        }
        if(!password) {            
            message += 'El campo de la contraseña está vacío.\n\n';
        }
        if(!confirmPassword) {            
            message += 'El campo de la confirmación de la contraseña está vacío.\n\n';
        }
        if(!email) {            
            message += 'El campo del email está vacío.\n\n';
        }
        if(password && confirmPassword && (password !== confirmPassword)) {
            message += 'Las dos contraseñas no coinciden.\n\n';
        }
        if(!phoneNumber) {            
            message += 'El campo del número del télefono está vacío.\n\n';
        }
        if(!rol) {            
            message += 'El campo del rol está vacío.\n\n';
        }
        if(rol == 'joven' && !emailParent1 && !emailParent2) {            
            message += 'Los campos de los emails están vacíos. Se debe rellenar al menos uno de ellos.\n\n';
        }

        if(message.length !== 0) {
            console.log(message);
            setVisibleModal(ModalType.Error, ModalTitle.ErrorTitle, message);
        }
        else {
            const data = {
                first_name:firstName,
                last_name:lastName,
                email:email,
                password:password,
                phone:phoneNumber,
                rol_slug:rol,
            }

            if (rol == 'joven') {
                // AÑADIR LOS EMAILS DE LOS PADRES
                data.email_parent_1 = emailParent1;
                data.email_parent_2 = emailParent2;
            }

            if (Platform.OS !== 'web') {
                data['expo_token'] = expoPushToken.data
            }

            await axiosInstance.post('/sivaria/v1/user/register', data)
                .then(function (response) {
                    //const token = response.data.data.token;
                    //console.log('Token JWT:', token);
                    
                    // Llamar función para resetear campos después del login exitoso

                    //console.log(response);
                    // Navegar a la siguiente pantalla (Home, por ejemplo)
                    //console.log('Registro exitoso');
                    
                    //navigation.navigate('Login');
                    let message = 'El usuairo se ha registrado correctamente';
                    setVisibleModal(ModalType.Information, ModalTitle.InformationTitle, message);

                })
                .catch(function (error) {
                    //console.log('Error de registro:', error);
                    //setModalTitle('ERROR');
                    //setModalMessage('Error en el registro');
                    //setModalVisible(true);
                    const message = 'Ha habido un error durante el proceso de registro del usuario. ' + error.response.data.data;
                    setVisibleModal(ModalType.Error, ModalTitle.ErrorTitle, message);
                    //Alert.alert('Error', 'Error en el registro. Inténtelo de nuevo.')
                });
        }
    }

    if(loading) {
        return (
            <LoadingScreen />
        );
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
            {/* Título */}
            <View style={{height: 200, alignItems: 'center', justifyContent: 'center'}}>
                <SivariaText isBold={true} fontSize={35}>SIVARIA</SivariaText>
                <SivariaText fontSize={20}>Formulario de registro</SivariaText>
            </View>
            
            <View style={{flex:1, backgroundColor: '#006E51', alignItems: 'center', justifyContent: 'center'}}>
                {/* Whitebox con inputs */}
                <View style={stylesSivaria.whiteBoxContainer}>
                    <View style={{height:80, alignItems:'center', justifyContent: 'center'}}>
                        <SivariaInput 
                            placeholder={'Nombre'}
                            value={firstName}
                            onChangeText={setFirstName}
                            autoCorrect={false}
                            autoCapitalize={'none'} 
                        />
                    </View>
                    <View style={{height:80, alignItems:'center', justifyContent: 'center'}}>
                        <SivariaInput 
                            placeholder={'Apellidos'}
                            value={lastName}
                            onChangeText={setLastName}
                            autoCorrect={false}
                            autoCapitalize={'none'} 
                        />
                    </View>
                    <View style={{height:80, alignItems:'center', justifyContent: 'center'}}>
                        <SivariaInput 
                            placeholder={'Email'}
                            value={email}
                            onChangeText={setEmail}
                            autoCorrect={false}
                            autoCapitalize={'none'} 
                        />
                    </View>
                    <View style={{height:70, alignItems:'center', justifyContent: 'center'}}>
                        <ShowHidePasswordInput 
                            placeholder='Contraseña' 
                            password={password} 
                            onChangeText={setPassword} />
                    </View>
                    <View style={{height:80, alignItems:'center', justifyContent: 'center'}}>
                        <ShowHidePasswordInput 
                            placeholder='Repetir Contraseña' 
                            password={confirmPassword} 
                            onChangeText={setConfirmPassword} />
                    </View>
                    <View style={{height:80,alignItems:'center', justifyContent: 'center'}}>
                        <SivariaInput 
                            placeholder={'Número de teléfono'}
                            value={phoneNumber}
                            onChangeText={setPhoneNumber}
                            autoCorrect={false}
                            autoCapitalize={'none'}
                            keyboardType={'phone-pad'} 
                        />
                    </View>
                    <View style={{height:80, alignItems:'center', justifyContent: 'center'}}>
                        <Dropdown 
                            items={roles}
                            placeholder={{ label: 'Selecciona un rol...', value: '0' }}
                            value={rol}
                            onValueChange={setRol}
                        />
                    </View>
                    {rol === 'joven' && (
                    <>
                        <View style={{height:80, alignItems:'center', justifyContent: 'center'}}>
                            <SivariaInput 
                                placeholder={'Email madre o figura parental'}
                                value={emailParent1}
                                onChangeText={setEmailParent1}
                                autoCorrect={false}
                                autoCapitalize={'none'} 
                            />
                        </View>
                        
                        <View style={{height:80, alignItems:'center', justifyContent: 'center'}}>
                            <SivariaInput 
                                placeholder={'Email padre o figura parental'}
                                value={emailParent2}
                                onChangeText={setEmailParent2}
                                autoCorrect={false}
                                autoCapitalize={'none'} 
                            />
                        </View>
                    </>
                    )}
                    <View style={{height:80, alignItems:'center', justifyContent:'center'}}>
                        <SivariaButton onPress={handleSubmit}>
                            <SivariaText isBold={true}>
                                ENVIAR
                            </SivariaText>
                        </SivariaButton>
                    </View>

                </View>
            </View>
    
            
        </Container>
      );
    };
    
    const styles = StyleSheet.create({
      scrollContainer: {
        flexGrow: 1,
      },
      container: {
        flex: 1,
      },
      titleView: {
        height: height * 0.1,
        backgroundColor: 'white',
        justifyContent: 'center',
        alignItems: 'center',
      },
      titleText: {
        fontSize: 20,
        fontWeight: 'bold',
      },
      whitebox: {
        backgroundColor: 'red',
        alignItems: 'center',
        justifyContent: 'center',
        paddingVertical: 20,
      },
      inputContainer: {
        width: '80%',
        backgroundColor: 'blue',
        paddingVertical: 20,
      },
      inputView: {
        height: 50,
        backgroundColor: 'steelblue',
        marginBottom: 10,
        justifyContent: 'center',
        paddingHorizontal: 10,
      },
      input: {
        color: 'white',
      },
      extraTextContainer: {
        marginTop: 20,
      },
      extraText: {
        color: 'white',
        marginBottom: 5,
      },
      button: {
        backgroundColor: 'green',
        padding: 10,
        alignItems: 'center',
        justifyContent: 'center',
        marginVertical: 10,
      },
      buttonText: {
        color: 'white',
        fontSize: 16,
      },
      footer: {
        height: height * 0.1,
        backgroundColor: 'black',
        justifyContent: 'center',
        alignItems: 'center',
      },
      footerText: {
        color: 'white',
      },
    });

export default RegisterScreen;