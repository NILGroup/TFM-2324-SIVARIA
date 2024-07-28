import React, { useEffect, useState } from 'react';
import { View, Dimensions, Text } from 'react-native';
import ShowHidePasswordInput from '../../components/show-hide-password-input';
import axiosInstance from '../../utils/axios-config-web';
import stylesSivaria from '../../styles/styles-sivaria';
import LoadingScreen from '../loading-screen';

import SivariaText from '../../components/sivaria-text';
import SivariaButton from '../../components/sivaria-button';
import Container from '../../components/component-containers/container';

import ModalComponent from '../../components/modal-component';

import useModal from '../../utils/modal-hook';
import { useToast } from 'react-native-toast-notifications';
import { removeItemLocalStorage, setItemLocalStorage } from '../../utils/general-local-storage';
import { AntDesign } from '@expo/vector-icons';

const { height } = Dimensions.get('window');

const RecoveryPasswordScreen = ({ route, navigation}) => {

  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const { email, token } = route.params;
  //console.log(email);
  //console.log(token);

  const [isLoading, setIsLoading] = useState(true);

    const [isDisabled, setIsDisabled] = useState(false);

  const [success, setSuccess] = useState(false);

  const toast = useToast();
  
  const { modalType, modalTitle, modalMessage, isVisible, setModalVisible, setVisibleModal } = useModal();
  
  useEffect(() => {
    
    function checkEnableButton(){
      if(email && token) {
        if(password && confirmPassword) 
        {
          setIsDisabled(false);
        }
        else {
          setIsDisabled(true);
        }
      }
    }
    checkEnableButton();
    setIsLoading(false);
  }, [password, confirmPassword]);


  async function changeUserPassword(e) {
    e.preventDefault();
    //setIsLoading(true);
    let message = '';
    if(!password) {            
      message += 'El campo de la contraseña está vacío.\n\n';
    }
    if(!confirmPassword) {            
      message += 'El campo de la confirmación de la contraseña está vacío.\n\n';
    }
    if(password && confirmPassword && password !== confirmPassword) {
      message += 'La contraseña no coincide con la confirmación de la contraseña.\n\n';
    }
    if(message.length !== 0) {
      toast.show(message,{type: 'danger'});
    }
    else {
      setIsLoading(true);
      const data = {
        password:password,
        confirm_password: confirmPassword
      }
      await setItemLocalStorage('userToken', token);
      await axiosInstance.put('/sivaria/v1/user/'+email+'/changeUserPassword', data)
      .then(function (response) {
        setIsLoading(false);
        let message = response.data.message;
        //setVisibleModal(ModalType.Information, ModalTitle.InformationTitle, message);
        toast.show(message,{type: 'success'});
        setSuccess(true);
      })
      .catch(function (error) {
        setIsLoading(false);
        
        let message = 'Error durante en el cambio de contraseña';
        if(error.response.data.message) {
          message += error.response.data.message;
        }
        //setVisibleModal(ModalType.Error, ModalTitle.ErrorTitle, message);
        //Alert.alert('Error', 'Error en el registro. Inténtelo de nuevo.')
        toast.show(message,{type: 'danger'});
      });
      
      await removeItemLocalStorage('userToken');
    }
  }

  if(!email || !token) {
    return (
      <Container>
        <SivariaText isBold={true} color={'white'}>
          { !email ? 'Email no especificado.'
                  : 'Acceso no autorizado.'
          }
        </SivariaText>
      </Container>
    );
  }

  if(isLoading) {
    return (
      <LoadingScreen />
    );
  }

  return (
    <Container>
        <ModalComponent 
            animationType='slide'
            setIsVisible={setModalVisible}
            isVisible={isVisible}
            title={modalTitle}
            modalType={modalType}
            message={modalMessage}
        />
        {/* Título */}
        <View style={{height: 200, alignItems: 'center', justifyContent: 'center'}}>
          <Text onPress={(e) => navigation.navigate('Login')} style={{color:'white', fontSize: 35, fontWeight: 'bold', textAlign: 'center'}}>SIVARIA</Text>
          <SivariaText fontSize={20}>Recuperación de contraseña</SivariaText>
        </View>
        <View style={{flex:1, backgroundColor: '#006E51', alignItems: 'center', justifyContent: 'center'}}>
            {/* Whitebox con inputs */}
            <View style={[stylesSivaria.whiteBoxContainer, {alignItems: 'center', justifyContent: 'center'}]}>
              {success ? 
                (<>
                  <View style={{width:'100%',height:70, alignItems: 'center', justifyContent: 'center'}}>
                    <View style={{width:'80%', alignItems: 'center', justifyContent: 'center'}}>
                      <AntDesign 
                          name={'checkcircle'} 
                          size={40} 
                          color={'#006E51'} 
                          style={{padding:10}}
                      />
                      <SivariaText color={'#006E51'} fontSize={25}>
                        La contraseña se ha actualizado correctamente. Vuelva a la página de Login para intentar iniciar sesión de nuevo. 
                      </SivariaText>
                    </View>
                  </View>
                </>)
                : 
                (<>
                  <View style={{width:'100%',height:70, alignItems: 'center', justifyContent: 'center'}}>
                    <View style={{width:'80%'}}>
                      <SivariaText color={'#006E51'} textAlign={'left'}>
                        Introduzca la nueva contraseña. Asegúrese de que las contraseñas en ambos campos coincidan. 
                      </SivariaText>
                    </View>
                  </View>
                  <View style={{width:'100%', height:70, alignItems:'center', justifyContent: 'center'}}>
                      <ShowHidePasswordInput 
                          placeholder='Contraseña' 
                          password={password} 
                          onChangeText={setPassword} />
                  </View>
                  <View style={{width: '100%', height:80, alignItems:'center', justifyContent: 'center'}}>
                      <ShowHidePasswordInput 
                          placeholder='Repetir Contraseña' 
                          password={confirmPassword} 
                          onChangeText={setConfirmPassword} />
                  </View>
                  <View style={{width:'100%', height:80, alignItems:'center', justifyContent:'center'}}>
                      <SivariaButton onPress={changeUserPassword} message={'CAMBIAR CONTRASEÑA'} disabled={isDisabled}/>
                  </View>
                </>)
              }
            </View>
        </View>

        
    </Container>
  );
};
    
export default RecoveryPasswordScreen;