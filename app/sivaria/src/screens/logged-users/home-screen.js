import { useEffect, useState } from 'react';
import { View, Text, Alert, SafeAreaView, Pressable } from 'react-native';
import axiosInstance from '../../utils/axios-config-web';
//import { useNavigation } from '@react-navigation/native';
import { getItemLocalStorage, removeItemLocalStorage } from '../../utils/general-local-storage';
import stylesSivaria from '../../styles/styles-sivaria';
import SivariaButton from '../../components/sivaria-button';
import Container from '../../components/component-containers/container';

import SivariaText from '../../components/sivaria-text';
import { useContext } from 'react';
import { AuthContext } from '../../context/auth-context';
import { ModalTitle, ModalType } from '../../utils/enum-types-modal';

import LoadingScreen from '../loading-screen';
import { useToast } from 'react-native-toast-notifications';
import { NavigationContainerRefContext } from '@react-navigation/native';
import { UserContext } from '../../context/user-context';

const HomeScreen = ({navigation}) => {
    const user = useContext(AuthContext);

    const userData = useContext(UserContext);

    const toast = useToast();

    const [isLoading, setIsLoading] = useState(false);

    async function sendPush(e) {
        e.preventDefault();
        setIsLoading(true);
        data = {
            email: await getItemLocalStorage('email'),
            notification_type: 'example'
        }
        await axiosInstance.post("/sivaria/v1/external/sendNotification", data)
        .then(async function (response) {
            //console.log('Push enviado exitosamente');
            let message = 'Push enviado exitosamente';
            toast.show(
                message,
                {
                    type: 'success'
                }
            );
            setIsLoading(false);
        })
        .catch(function (error) {
            let message = 'Error en el envío de la notificación del usuario';
            //setVisibleModal(ModalType.Error, ModalTitle.ErrorTitle, message);
            toast.show(
                message,
                {
                    type: 'danger'
                }
            );
            setIsLoading(false);
        });
    }

    function goToQuestionnaire(e) {
        //console.log(userData);
        if(userData.rolSlug == 'joven') {
            navigation.navigate('YoungstersQuestionnaireSivaria');
        }
        else if (userData.rolSlug == 'padre' || userData.rol == 'madre') {
            navigation.navigate('ParentsQuestionnaireSivaria');
        }
        else if (userData.rolSlug == 'profesional') {
            navigation.navigate('ProfessionalQuestionnaireSivaria');
        }
    }

    if(isLoading) {
        return (
            <LoadingScreen />
        );
    }

    return (
      <Container>
        <View style={{flex:1, backgroundColor: 'white'}}>
            <View style={{flex:1, width: '100%', alignItems:'center', justifyContent: 'center'}}>
                <View style={{flex:1, width: '80%', alignItems: 'center', justifyContent: 'center'}}>
                    <SivariaButton onPress={(e) => sendPush(e)} message={'ENVIAR PUSH'} />
                </View>
            </View>
        </View>
        <View style={{flex:1, backgroundColor: 'white'}}>
            <View style={{flex:1, width: '100%', alignItems:'center', justifyContent: 'center'}}>
                <View style={{flex:1, width: '80%', alignItems: 'center', justifyContent: 'center'}}>
                    <SivariaButton onPress={(e) => goToQuestionnaire(e)} message={'COMENZAR CUESTIONARIO'} />
                </View>
            </View>
        </View>
      </Container>
  );
}
  
export default HomeScreen;