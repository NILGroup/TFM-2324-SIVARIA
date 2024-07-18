import React, { useEffect, useState } from 'react';
import { StyleSheet, View, Text, Dimensions, Platform } from 'react-native';
import Dropdown from '../../components/dropdown';
import ShowHidePasswordInput from '../../components/show-hide-password-input';
import axiosInstance from '../../utils/axios-config-web';
import stylesSivaria from '../../styles/styles-sivaria';
import LoadingScreen from '../loading-screen';

import SivariaText from '../../components/sivaria-text';
import SivariaInput from '../../components/sivaria-input';
import SivariaButton from '../../components/sivaria-button';
import Container from '../../components/component-containers/container';

import ModalComponent from '../../components/modal-component';

import { usePushNotifications } from '../../utils/use-push-notifications';

import useModal from '../../utils/modal-hook';
import { useToast } from 'react-native-toast-notifications';
import SivariaSpanishPhoneInput from '../../components/sivaria-spanish-phone-input';

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

    const [isLoading, setIsLoading] = useState(false);

    const [isDisabled, setIsDisabled] = useState(true);


    const [showExtraText, setShowExtraText] = useState(false);
    
    const {expoPushToken, notification} = usePushNotifications();

    const toast = useToast();
    
    const { modalType, modalTitle, modalMessage, isVisible, setModalVisible, setVisibleModal } = useModal();

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
                //setVisibleModal(ModalType.Error, ModalTitle.ErrorTitle, message)
                toast.show(
                    message,
                    {
                        type: 'danger'
                    }
                );
            });

            setIsLoading(false);

        };
        
        setIsLoading(true);
        fetchRoles();
      }, []
    );
    
    useEffect(() => {
        // AÑADIR VALIDACIONES
        if(firstName && 
            lastName &&
            email &&
            password &&
            confirmPassword &&
            phoneNumber &&
            rol &&
            emailParent1 &&
            emailParent2) 
        {
            setIsDisabled(true);
        }
    }, [firstName, lastName, email, password, confirmPassword, phoneNumber, rol, emailParent1, emailParent2]);


    async function handleSubmit(e) {
        e.preventDefault();
        //setIsLoading(true);
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
        else if(phoneNumber && isNaN(phoneNumber)) {
            message += 'El número de teléfono introducido no es numérico.\n\n';
        }
        else if(phoneNumber && !isNaN(phoneNumber) && (phoneNumber.length !== 9)) {
            message += 'El número de teléfono introducido no tiene 9 dígitos';
        }
        else if(phoneNumber && !isNaN(phoneNumber) && (!phoneNumber.startsWith('6') && !phoneNumber.startsWith('7'))) {
            message += 'El número de teléfono introducido no empieza con 6 o 7';
        }
        if(!rol) {            
            message += 'El campo del rol está vacío.\n\n';
        }
        if(rol == 'joven' && !emailParent1 && !emailParent2) {            
            message += 'Los campos de los emails están vacíos. Se debe rellenar al menos uno de ellos.\n\n';
        }

        if(message.length !== 0) {
            //setIsLoading(false);
            toast.show(
                message,
                {
                    type: 'danger'
                }
            );
            //setVisibleModal(ModalType.Error, ModalTitle.ErrorTitle, message);
        }
        else {
            console.log('LOGEADO');
            /*
            setIsLoading(true);
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
                    setIsLoading(false);
                    let message = 'El usuario se ha registrado correctamente';
                    //setVisibleModal(ModalType.Information, ModalTitle.InformationTitle, message);
                    toast.show(
                        message,
                        {
                            type: 'success'
                        }
                    );

                })
                .catch(function (error) {
                    setIsLoading(false);
                    let message = 'Ha habido un error durante el proceso de registro del usuario. ' + error.response.data.data;
                    //setVisibleModal(ModalType.Error, ModalTitle.ErrorTitle, message);
                    //Alert.alert('Error', 'Error en el registro. Inténtelo de nuevo.')
                    toast.show(
                        message,
                        {
                            type: 'danger'
                        }
                    );
                });
                */
        }
    }

    useEffect(() => {
        function enableRegisterButton(){
            if(firstName && 
                lastName && 
                email && 
                password && 
                confirmPassword &&
                rol
            ) {
                const areFieldsFilled = firstName && lastName && email && password && confirmPassword && rol;

                if (!areFieldsFilled) {
                    setIsDisabled(true);
                    return;
                }

                const isRoleValid = rol === 'joven' ? (emailParent1 || emailParent2) : rol !== '0';

                setIsDisabled(!isRoleValid);
            }
        }
        enableRegisterButton();
    }, [firstName, lastName, email, password, confirmPassword, phoneNumber, rol, emailParent1, emailParent2]);

    if(isLoading) {
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
                <Text onPress={(e) => navigation.navigate('Login')} style={{color:'white', fontSize: 35, fontWeight: 'bold', textAlign: 'center'}}>SIVARIA</Text>
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
                            inputMode={'email'}
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
                        <SivariaSpanishPhoneInput 
                            placeholder={'Número de teléfono'}
                            phoneNumber={phoneNumber}
                            onChangeText={setPhoneNumber}
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
                                placeholder={'Email de figura parental 1'}
                                value={emailParent1}
                                onChangeText={setEmailParent1}
                                autoCorrect={false}
                                autoCapitalize={'none'} 
                                inputMode={'email'}
                            />
                        </View>
                        
                        <View style={{height:80, alignItems:'center', justifyContent: 'center'}}>
                            <SivariaInput 
                                placeholder={'Email de figura parental 2'}
                                value={emailParent2}
                                onChangeText={setEmailParent2}
                                autoCorrect={false}
                                autoCapitalize={'none'} 
                                inputMode={'email'}
                            />
                        </View>
                    </>
                    )}
                    <View style={{height:80, alignItems:'center', justifyContent:'center'}}>
                        <SivariaButton onPress={handleSubmit} message={'ENVIAR'} disabled={isDisabled}/>
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