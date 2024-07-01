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
        //backgroundColor:'red',
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
        flex: 1,
        backgroundColor: 'white',
        justifyContent: 'center',
        alignItems: 'center',
        //width: '80%', // Ancho del formulario relativo al tamaño de la pantalla
        //width: 350,
        borderRadius: 8, 
        //paddingHorizontal: '5%', // MODIFICAR PARA AJUSTAR EL TAMAÑO
        //paddingVertical: '20%', // MODIFICAR PARA AJUSTAR EL TAMAÑO
        borderColor: '#ccc',
        borderWidth: 5
    },
    input: {
        //width: '100%',
        height: 40,
        borderWidth: 1,
        borderColor: '#ccc',
        marginBottom: 10,
        paddingHorizontal: 10,
        color:'#333',
        fontSize: 16,
    },
    button: {
        //width: Platform.OS !== 'web' ? '75%' : '25%',
        //backgroundColor: '#006E51',
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










    // NUEVOS ESTILOS
    safeAreaViewContainer: {
        flex:1, 
        backgroundColor: '#006E51',
        paddingTop: Platform.OS === 'android' ? StatusBarManager.HEIGHT : 0,
    },
    whiteBoxContainer: {
        flex:1,
        backgroundColor: 'white',
        width: '80%',
        borderRadius: 8,
        borderColor: '#ccc',
        borderWidth: 5,
    },
    mainContainer: {
        flex:1,
        alignItems: 'center',
        justifyContent: 'center',
    },
    greenMainContainer: {
        flex: 1, 
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: '#006E51',
    },
    flex3: {
        flex:3
    },
    flex05: {
        flex:0.5
    },





    whiteBoxContainerGrow: {
        flexGrow:1,
        backgroundColor: 'white',
        width: '80%',
        borderRadius: 8,
        borderColor: '#ccc',
        borderWidth: 5,
    },
    mainContainerGrow: {
        flexGrow:1,
        alignItems: 'center',
        justifyContent: 'center',
    },
    greenMainContainerGrow: {
        flexGrow: 1, 
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: '#006E51',
    },
    flexGrow3: {
        flexGrow:3
    },
    flexGrow05: {
        flexGrow:0.5
    },
});

export default stylesSivaria;