import { StyleSheet, Platform, NativeModules} from "react-native";

const { StatusBarManager } = NativeModules;

const stylesSivaria = StyleSheet.create({
    tabContainer: {
        justifyContent: 'center',
        alignItems: 'center',
        paddingTop: Platform.OS === 'android' ? StatusBarManager.HEIGHT : 0,
    },
    container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#006E51',
        paddingTop: Platform.OS === 'android' ? StatusBarManager.HEIGHT : 0,
    },
    header: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    title: {
        fontSize: 40,
        fontWeight: 'bold',
        color: 'white'
    },
    formContainer: {
        flex: 2,
        backgroundColor: 'white',
        justifyContent: 'center',
        alignItems: 'center',
        width: '80%', // Ancho del formulario relativo al tamaño de la pantalla
        borderRadius: 8, 
        paddingHorizontal: '5%', 
        paddingVertical: '20%',
        borderColor: '#ccc',
        borderWidth: 5
    },
    input: {
        width: '80%',
        height: 40,
        borderWidth: 1,
        borderColor: '#ccc',
        marginBottom: 10,
        paddingHorizontal: 10,
        color:'#333',
        fontSize: 16,
    },
    button: {
        width: Platform.OS !== 'web' ? '75%' : '25%',
        backgroundColor: '#006E51',
        padding: 10,
        alignItems: 'center',
        borderRadius: 5,
        marginTop: 10,
    },
    buttonText: {
        color: 'white',
        fontSize: 16,
    },
    formContainerScrollView: {
        flex: 2,
        backgroundColor: 'white',
        justifyContent: 'center',
        alignItems: 'center',
        width: '80%', // Ancho del formulario relativo al tamaño de la pantalla
        borderRadius: 8, 
        paddingHorizontal: '5%', 
        paddingVertical: '2%',
        borderColor: '#ccc',
        borderWidth: 5
    },
    footer: {
        flex:0.5,
        justifyContent: 'center',
        alignItems: 'center',
    },
    loading: {
        flex: 1,
        padding: 16,
        justifyContent: 'center',
        alignItems: 'center',
    },
});

export default stylesSivaria;