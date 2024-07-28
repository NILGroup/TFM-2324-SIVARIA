import React, { useState } from "react";
import { TextInput, StyleSheet, View } from "react-native";
import { MaterialCommunityIcons } from "@expo/vector-icons";

const ShowHidePasswordInput = ({placeholder, password, onChangeText}) => {

    const [showPassword, setShowPassword] = useState(false);

    const toggleShowPassword = () => {
        setShowPassword(!showPassword);
    };

    return(
        <View style={styles.hideShowContainer}>
            <TextInput
                secureTextEntry={!showPassword} 
                value={password} 
                onChangeText={onChangeText} 
                style={styles.input} 
                placeholder={placeholder}
                placeholderTextColor="#aaa"
                autoCorrect={false}
                autoCapitalize="none"
                autoComplete="off"
            /> 
            <MaterialCommunityIcons 
                name={showPassword ? 'eye-off' : 'eye'} 
                size={24} 
                color="#aaa"
                style={styles.icon} 
                onPress={toggleShowPassword} 
            /> 
        </View>
    );

}

const styles = StyleSheet.create({ 
    hideShowContainer: { 
        flexDirection: 'row', // para alinear el icono con el input
        alignItems: 'center', 
        justifyContent: 'center', 
        backgroundColor: '#f3f3f3', 
        borderRadius: 8, 
        paddingHorizontal: 14, 

        width: '80%',
        borderWidth: 1,
        borderColor: '#ccc',
    }, 
    prueba: {
        width: '80%',
        height: 40,
        borderWidth: 1,
        borderColor: '#ccc',
        marginBottom: 10,
        paddingHorizontal: 10,
        color:'#333',
        fontSize: 16,
    },
    input: { 
        flex: 1, 
        color: '#333', 
        paddingVertical: 10, 
        paddingRight: 10, 
        fontSize: 16
    }, 
    icon: { 
        marginLeft: 10, 
    },
}); 

export default ShowHidePasswordInput;