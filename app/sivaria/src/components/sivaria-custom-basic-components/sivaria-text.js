import { Text, StyleSheet } from "react-native";


const SivariaText = ({color, isBold, fontSize, children, textAlign}) => {
    return(
        <Text style={styles(color, isBold, fontSize, textAlign).text}>
            {children}
        </Text>
    );
}

const styles = (color, isBold, fontSize, textAlign) => StyleSheet.create({ 
    text:{
        color: color ? color : 'white',
        fontWeight: isBold ? 'bold' : 'normal',
        fontSize: fontSize ? fontSize : 15,
        textAlign: textAlign ? textAlign : 'center',
    }
}); 

export default SivariaText;