import React, { useState } from 'react';
import { SafeAreaView, View, Text, TextInput, Pressable, Alert } from 'react-native';
import RNPickerSelect from 'react-native-picker-select';



const RegisterScreen = () => {

    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [phoneNumber, setPhoneNumber] = useState('');
    const [rol, setRol] = useState('');
    const [phoneNumberParent1, setPhoneNumberParent1] = useState('');
    const [phoneNumberParent2, setPhoneNumberParent2] = useState('');

    const [roles, setRoles] = useState([]);

    return (
        <SafeAreaView>
            <ScrollView>
                <TextInput
                value={firstName}
                onChangeText={setFirstName}
                placeholder="Nombre"
                autoCorrect={false}
                autoCapitalize='none'
                />
                <TextInput
                value={lastName}
                onChangeText={setLastName}
                placeholder="Apellidos"
                autoCorrect={false}
                autoCapitalize='none'
                />
                <TextInput
                placeholder='Email'
                value={email}
                onChangeText={setEmail}
                autoCorrect={false}
                autoCapitalize='none'
                />
                <TextInput
                placeholder='Contraseña'
                secureTextEntry
                value={password}
                onChangeText={setPassword}
                autoCorrect={false}
                autoCapitalize='none'
                />
                <TextInput
                placeholder='Repetir Contraseña'
                secureTextEntry
                value={confirmPassword}
                onChangeText={setConfirmPassword}
                autoCorrect={false}
                autoCapitalize='none'
                />
                <TextInput
                value={phoneNumber}
                onChangeText={setPhoneNumber}
                placeholder="Número de teléfono"
                keyboardType="phone-pad"
                />
                <RNPickerSelect
                items={roles}
                placeholder={{ label: 'Selecciona un rol...', value: '0' }}
                value={rol}
                onValueChange={(value) => setRol(value)}
                />
                {rol === 'joven' && (
                <>
                    <TextInput
                    placeholder="Teléfono madre o figura parental"
                    value={phoneNumberParent1}
                    onChangeText={setPhoneNumberParent1}
                    keyboardType="phone-pad"
                    />
                    <TextInput
                    placeholder="Teléfono padre o figura parental"
                    value={phoneNumberParent2}
                    onChangeText={setPhoneNumberParent2}
                    keyboardType="phone-pad"
                    />
                </>
                )}

                <Pressable onPress={handleSubmit}>
                    <Text>Enviar</Text>
                </Pressable>
            </ScrollView>
        </SafeAreaView>
    );
}
  
export default RegisterScreen;