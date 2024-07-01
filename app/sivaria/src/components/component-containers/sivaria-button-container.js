import { View, StyleSheet } from "react-native";
import SivariaButton from "../sivaria-custom-basic-components/sivaria-button";

const SivariaButtonContainer = ({children}) => {
    return(
        <View style={stylesSivariaButtonContainer.sivariaButtonContainer}>
            {children}
        </View>
    );
}

const stylesSivariaButtonContainer = StyleSheet.create({
        sivariaButtonContainer: {
            flex:1,
            alignItems: 'center',
            justifyContent: 'center',
        }
    }
);

export default SivariaButtonContainer;