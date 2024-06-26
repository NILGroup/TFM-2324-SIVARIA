import React, { useEffect, useState } from 'react';
import { StyleSheet, ActivityIndicator, ScrollView, SafeAreaView, View, Text, TextInput, Pressable, Alert } from 'react-native';
import Dropdown from '../components/dropdown';
import ShowHidePasswordInput from '../components/show-hide-password-input';
import axiosInstance from '../utils/axios-config-web';
import stylesSivaria from '../styles/styles-sivaria';
import PhoneInput from "react-native-phone-input";
import LoadingScreen from './loading-screen';

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

    useEffect(() => {
        //console.log('entrando a buscar roles');
        //console.log(axiosInstance.defaults.baseURL + '/sivaria/v1/rol');
        const fetchRoles = async () => {
            await axiosInstance.get('/sivaria/v1/rol')
            .then(function (response) {
                const rolesData = response.data.data.rols.map(role => ({
                    label: role.description, // Ajusta esto según la estructura de tu JSON
                    value: role.slug // Ajusta esto según la estructura de tu JSON
                }));
                //console.log(rolesData);
                setRoles(rolesData);
            })
            .catch(function (error) {
                console.log(error);
                Alert.alert('Error', 'Hubo un problema al obtener los roles');
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
    const handleSubmit = async () => {
        const data = {
            first_name:firstName,
            last_name:lastName,
            email:email,
            password:password,
            phone:phoneNumber,
            rol_slug:rol,
        }

        if (rol == 'joven') {
            // AÑADIR LOS NUMEROS DE LOS PADRES
            data.email_parent_1 = emailParent1;
            data.email_parent_2 = emailParent2;
        }

        await axiosInstance.post('/sivaria/v1/user/register', data)
            .then(function (response) {
                //const token = response.data.data.token;
                //console.log('Token JWT:', token);
                
                // Llamar función para resetear campos después del login exitoso

                console.log(response);
                // Navegar a la siguiente pantalla (Home, por ejemplo)
                console.log('Registro exitoso');
                
                navigation.navigate('Login');
            })
            .catch(function (error) {
                console.log('Error de registro:', error);
                Alert.alert('Error', 'Error en el registro. Inténtelo de nuevo.')
            });
    }

    if(loading) {
        return (
            <LoadingScreen />
        );
    }

    return (
        <SafeAreaView style={stylesSivaria.container}>
            <View style={stylesSivaria.header}>
                <Text style={stylesSivaria.title}>Sivaria</Text>
                <Text style={stylesSivaria.buttonText}>Regístrese</Text>
            </View>
            <View style={stylesSivaria.formContainer}>
                <TextInput
                style={stylesSivaria.input}
                value={firstName}
                onChangeText={setFirstName}
                placeholder="Nombre"
                placeholderTextColor='#ccc'
                autoCorrect={false}
                autoCapitalize='none'
                />
                <TextInput
                style={stylesSivaria.input}
                value={lastName}
                onChangeText={setLastName}
                placeholder="Apellidos"
                placeholderTextColor='#ccc'
                autoCorrect={false}
                autoCapitalize='none'
                />
                <TextInput
                style={stylesSivaria.input}
                placeholder='Email'
                placeholderTextColor='#ccc'
                value={email}
                onChangeText={setEmail}
                autoCorrect={false}
                autoCapitalize='none'
                />
                <ShowHidePasswordInput placeholder='Contraseña' password={password} onChangeText={setPassword} />
                <ShowHidePasswordInput placeholder='Repetir Contraseña' password={confirmPassword} onChangeText={setConfirmPassword} />
                <TextInput
                style={stylesSivaria.input}
                value={phoneNumber}
                onChangeText={setPhoneNumber}
                placeholder="Número de teléfono"
                placeholderTextColor='#ccc'
                keyboardType="phone-pad"
                />
                <Dropdown 
                items={roles}
                placeholder={{ label: 'Selecciona un rol...', value: '0' }}
                value={rol}
                onValueChange={setRol}
                />
                {rol === 'joven' && (
                <>
                    <TextInput
                    style={stylesSivaria.input}
                    placeholder="Email madre o figura parental"
                    placeholderTextColor='#ccc'
                    value={emailParent1}
                    onChangeText={setEmailParent1}
                    autoCorrect={false}
                    autoCapitalize='none'
                    />
                    <TextInput
                    style={stylesSivaria.input}
                    placeholderTextColor='#ccc'
                    placeholder="Email padre o figura parental"
                    value={emailParent2}
                    onChangeText={setEmailParent2}
                    autoCorrect={false}
                    autoCapitalize='none'
                    />
                </>
                )}

                <Pressable 
                    style={stylesSivaria.button}
                    onPress={handleSubmit}>
                    <Text style={stylesSivaria.buttonText}>Enviar</Text>
                </Pressable>
            </View>
            <View style={stylesSivaria.footer}></View>
        </SafeAreaView>
    );
}

export default RegisterScreen;