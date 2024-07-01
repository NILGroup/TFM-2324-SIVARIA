import { TextInput, View, StyleSheet } from "react-native";


const SivariaInput = ({placeholder, value, onChangeText, autoCorrect, autoCapitalize, keyboardType}) => {
    return(
        <View style={styles.inputContainer}>
            <TextInput
                style={styles.input} 
                placeholder={placeholder}
                placeholderTextColor={'#aaa'}
                value={value} 
                onChangeText={onChangeText} 
                autoCorrect={autoCorrect ? autoCorrect : false}
                autoCapitalize={autoCapitalize ? autoCapitalize : 'none'}
                keyboardType= {keyboardType ? keyboardType : 'default'}
            />
        </View> 
    );
}

const styles = StyleSheet.create({ 
    inputContainer:{
        backgroundColor: '#f3f3f3', 
        borderRadius: 8, 
        paddingHorizontal: 14, 
        height: 45,
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
    }
}); 

export default SivariaInput;