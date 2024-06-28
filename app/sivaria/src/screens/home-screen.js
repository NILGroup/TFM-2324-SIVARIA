import { View, Text, Alert, SafeAreaView, Pressable } from 'react-native';
import axiosInstance from '../utils/axios-config-web';
//import { useNavigation } from '@react-navigation/native';
import { getItemLocalStorage, removeItemLocalStorage } from '../utils/general-local-storage';
import stylesSivaria from '../styles/styles-sivaria';

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
            email: getItemLocalStorage('email'),
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
      <SafeAreaView>
        <Text>Home Screen</Text>
        <View>
              <Pressable 
                onPress={(e) => callLogout(e)}>
                  <Text>Cerrar sesión</Text>
              </Pressable>
        </View>
        <View>
            <Pressable 
                style={stylesSivaria.button}
                onPress={(e) => sendPush(e)}>
                <Text style={stylesSivaria.buttonText}>Enviar push</Text>
            </Pressable>
        </View>
      </SafeAreaView>
  );
}
  
export default HomeScreen;