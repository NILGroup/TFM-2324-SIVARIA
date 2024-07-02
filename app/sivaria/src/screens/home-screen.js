import { View, Text, Alert, SafeAreaView, Pressable } from 'react-native';
import axiosInstance from '../utils/axios-config-web';
//import { useNavigation } from '@react-navigation/native';
import { getItemLocalStorage, removeItemLocalStorage } from '../utils/general-local-storage';
import stylesSivaria from '../styles/styles-sivaria';
import SivariaButton from '../components/sivaria-custom-basic-components/sivaria-button';
import Container from '../components/component-containers/container';

import SivariaText from '../components/sivaria-custom-basic-components/sivaria-text';
import { useContext } from 'react';
import { AuthContext } from '../context/auth-context';
import { ModalTitle, ModalType } from '../utils/enum-types-modal';

const HomeScreen = ({navigation}) => {
    const { setIsAuthenticated } = useContext(AuthContext);

    async function callLogout(e) {
        e.preventDefault();
        await axiosInstance.post("/sivaria/v1/user/logout")
        .then(async function (response) {
            //const token = getLocalStorage('userToken');
            //console.log(token);
            //console.log('Logout exitoso');
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
            console.log('Push enviado exitosamente');
        })
        .catch(function (error) {
            let message = 'Ha habido un error enviando la notificación al usuario.';
            setVisibleModal(ModalType.Error, ModalTitle.ErrorTitle, message);
        });
    }

  return (
      <Container>
        <View style={{flex:1, backgroundColor: 'white'}}>
            <View style={{flex:1, width: '100%', backgroundColor: 'black', alignItems:'center', justifyContent: 'center'}}>
                <View style={{flex:1, width: '80%', alignItems: 'center', justifyContent: 'center', backgroundColor: 'red'}}>
                    <SivariaButton onPress={(e) => callLogout(e)}>
                        <SivariaText isBold={true}>
                            CERRAR SESIÓN
                        </SivariaText>
                    </SivariaButton>
                </View>
            </View>
            <View style={{flex:1, width: '100%', alignItems:'center', justifyContent: 'center'}}>
                <View style={{flex:1, alignItems: 'center', justifyContent: 'center', backgroundColor: 'red'}}>
                    <SivariaButton onPress={(e) => sendPush(e)}>
                        <SivariaText isBold={true}>
                            ENVIAR PUSH
                        </SivariaText>
                    </SivariaButton>
                </View>
            </View>
        </View>
      </Container>
  );
}
  
export default HomeScreen;