import { View, Text, Alert, SafeAreaView, Pressable } from 'react-native';
import axiosInstance from '../utils/axios-config-web';
//import { useNavigation } from '@react-navigation/native';
import { getItemLocalStorage, removeItemLocalStorage } from '../utils/general-local-storage';
import stylesSivaria from '../styles/styles-sivaria';
import SivariaButton from '../components/sivaria-custom-basic-components/sivaria-button';
import Container from '../components/component-containers/container';

import SivariaText from '../components/sivaria-custom-basic-components/sivaria-text';

const HomeScreen = ({navigation, route}) => {
    const { setIsAuthenticated } = route.params;

    async function callLogout(e) {
        e.preventDefault();
        await axiosInstance.post("/sivaria/v1/user/logout")
        .then(async function (response) {
            //const token = getLocalStorage('userToken');
            //console.log(token);
            console.log('Logout exitoso');
            removeItemLocalStorage('userToken');
            removeItemLocalStorage('email');
            //const tokenI = getLocalStorage('userToken');
            //console.log(tokenI);
            //removeItemLocalStorage('userToken');
            //navigation.navigate('Login');
            setIsAuthenticated(false);
        })
        .catch(function (error) {
            console.log(error);
        });
    }

    
    async function sendPush(e) {
        e.preventDefault();
        data = {
            email: await getItemLocalStorage('email'),
            notification_type: 'example'
        }
        await axiosInstance.post("/sivaria/v1/external/sendNotification", data)
        .then(async function (response) {
            //const token = getLocalStorage('userToken');
            //console.log(token);
            console.log('Push enviado exitosamente');
            //const tokenI = getLocalStorage('userToken');
            //console.log(tokenI);
            //removeItemLocalStorage('userToken');
            //navigation.navigate('Login');
        })
        .catch(function (error) {
            console.log(error);
        });
    }

  return (
      <Container>
        <View style={{backgroundColor: 'white', alignItems: 'center', justifyContent: 'center'}}>
            <View style={{width: '100%', alignItems:'center', justifyContent: 'center'}}>
                <SivariaButton onPress={(e) => callLogout(e)}>
                    <SivariaText isBold={true}>
                        CERRAR SESIÓN
                    </SivariaText>
                </SivariaButton>
            </View>
            <View style={{width: '100%', alignItems:'center', justifyContent: 'center'}}>
                <SivariaButton onPress={(e) => sendPush(e)}>
                    <SivariaText isBold={true}>
                        ENVIAR PUSH
                    </SivariaText>
                </SivariaButton>
            </View>
        </View>
      </Container>
  );
}
  
export default HomeScreen;