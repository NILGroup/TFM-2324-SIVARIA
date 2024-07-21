import React, { useState } from "react";
import { TextInput, StyleSheet, View, Text } from "react-native";
import stylesInput from "../styles/styles-input";
import stylesIcon from "../styles/styles-icon";

import SpainFlag from "../assets/svg/flag-for-flag-spain-svgrepo-com.svg";

const SivariaSpanishPhoneInput = ({placeholder, phoneNumber, onChangeText}) => {
    return(
        <View style={styles.hideShowContainer}>
             {/*<MaterialCommunityIcons 
                name={showPassword ? 'eye-off' : 'eye'} 
                size={24} 
                color="#aaa"
                style={styles.icon} 
            />*/} 
            <SpainFlag width={20} height={20} />
            <Text style={styles.prefixNumber}>+34</Text>
            <TextInput
                inputMode="numeric"
                value={phoneNumber} 
                onChangeText={onChangeText} 
                style={styles.input} 
                placeholder={placeholder}
                placeholderTextColor="#aaa"
                autoCorrect={false}
                autoCapitalize="none"
                autoComplete="off"
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
    input: { 
        flex: 1, 
        color: '#333', 
        paddingVertical: 10, 
        paddingRight: 10, 
        fontSize: 16,
        borderLeftColor: '#ccc',
        borderLeftWidth: 2
    }, 
    prefixNumber: { 
        marginRight: 10, 
        marginLeft: 5,
        fontSize:18,
        color: '#aaa',
    },
}); 

export default SivariaSpanishPhoneInput;