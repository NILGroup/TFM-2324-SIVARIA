import axios from 'axios';
import { Text, TextInput, View, SafeAreaView, Pressable, Platform, NativeModules } from 'react-native';
import React, { useState } from 'react';
import { useNavigation } from '@react-navigation/native';

const { StatusBarManager } = NativeModules;

const LoginScreen = () => {
    const navigation = useNavigation();
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const callLogin = () => {
        const data = {
            email: email,
            password: password
        };

        axios.post('http://127.0.0.1:8000/sivaria/v1/user/login', data)
            .then(function (response) {
                const token = response.data.data.token;
                console.log('Token JWT:', token);
                
                // Llamar función para resetear campos después del login exitoso
                setEmail('');
                setPassword('');
                
                // Navegar a la siguiente pantalla (Dashboard, por ejemplo)
                //navigation.navigate('Dashboard');
                console.log('Logeo exitoso');
            })
            .catch(function (error) {
                console.log('Error de inicio de sesión:', error);
            });
    };


    return (
        <SafeAreaView style = {{
            flex: 1,
            paddingTop: Platform.OS === 'android' ? StatusBarManager.HEIGHT : 0,
        }}>
            <View>
                <Text>SIVARIA</Text>
                <TextInput
                            placeholder='Email' 
                            value={email} 
                            onChangeText={setEmail} 
                            autoCorrect={false}
                            autoCapitalize='none' />
                
                <TextInput
                            placeholder='Contraseña' 
                            secureTextEntry 
                            value={password} 
                            onChangeText={setPassword} 
                            autoCorrect={false}
                            autoCapitalize='none'/>
            </View>
            <View>
                <Pressable onPress={() => callLogin()}>
                    <Text>Iniciar sesión</Text>
                </Pressable>
            </View>
            <View>
                <Text>Registrarse</Text>
            </View>
            
        </SafeAreaView>
    );
}

export default LoginScreen;