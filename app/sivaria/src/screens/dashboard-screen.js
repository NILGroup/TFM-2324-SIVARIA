import { View, Text, Alert, SafeAreaView, Pressable } from 'react-native';
import axiosInstance from '../utils/axios-config-web';
import { useNavigation } from '@react-navigation/native';

const DashboardScreen = ({navigation}) => {

  const callLogout = () => {
    console.log(axiosInstance.defaults.withCredentials);

    axiosInstance.post('/sivaria/v1/user/logout', {withCredentials: true})
        .then(function (response) {
            // Navegar a la siguiente pantalla (Dashboard, por ejemplo)
            console.log('Logout exitoso');
            const setCookieHeader = response.headers['set-cookie'];
            console.log('Cookie received', setCookieHeader);
            axiosInstance.defaults.withCredentials = false;
            navigation.navigate('Login');
        })
        .catch(function (error) {
            console.log('Error en el cierre de sesión:', error);
            Alert.alert('Error', 'Error en en el cierre de sesión.')
        });
};

  return (
      <SafeAreaView>
        <Text>Dashboard Screen</Text>
        <View>
              <Pressable onPress={() => callLogout()}>
                  <Text>Cerrar sesión</Text>
              </Pressable>
          </View>
      </SafeAreaView>
  );
}
  
export default DashboardScreen;