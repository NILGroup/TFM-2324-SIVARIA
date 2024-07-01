import { StyleSheet, Platform, NativeModules} from "react-native";

const { StatusBarManager } = NativeModules;

const stylesSivariaModal = StyleSheet.create({
    modalButtonContainer: {
        //backgroundColor: 'black', 
        width: '30%', 
        alignItems: 'center'
    },
    modalButton: {
        padding: 10,
        alignItems: 'center',
        borderRadius: 5,
        marginTop: 10,
    },
    modalButtonText: {
        color: 'white',
        fontSize: 16,
    },
});

export default stylesSivariaModal;