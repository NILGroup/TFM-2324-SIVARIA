import { Text, StyleSheet } from "react-native";


const SivariaText = ({color, isBold, fontSize, children, textAlign, isItalic}) => {
    return(
        <Text style={styles(color, isBold, fontSize, textAlign, isItalic).text}>
            {children}
        </Text>
    );
}

const styles = (color, isBold, fontSize, textAlign, isItalic) => StyleSheet.create({ 
    text:{
        color: color ? color : 'white',
        fontWeight: isBold ? 'bold' : 'normal',
        fontSize: fontSize ? fontSize : 15,
        textAlign: textAlign ? textAlign : 'center',
        fontStyle: isItalic ? 'italic' : 'normal',
    }
}); 

export default SivariaText;