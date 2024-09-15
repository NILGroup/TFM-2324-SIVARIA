import React, { useEffect, useState } from 'react';
import { View, Text, Dimensions } from 'react-native';
import axiosInstance from '../../utils/axios-config-web';
import stylesSivaria from '../../styles/styles-sivaria';
import LoadingScreen from '../loading-screen';

import SivariaText from '../../components/sivaria-text';
import SivariaInput from '../../components/sivaria-input';
import SivariaButton from '../../components/sivaria-button';
import Container from '../../components/component-containers/container';

import ModalComponent from '../../components/modal-component';

import useModal from '../../utils/modal-hook';
import { useToast } from 'react-native-toast-notifications';

const { height } = Dimensions.get('window');

const ForgotPasswordScreen = ({navigation}) => {

  const [email, setEmail] = useState('');

  const [isLoading, setIsLoading] = useState(false);

  const [isDisabled, setIsDisabled] = useState(true);

  const toast = useToast();
  
  const { modalType, modalTitle, modalMessage, isVisible, setModalVisible, setVisibleModal } = useModal();
  
  useEffect(() => {
      if(email) {
          setIsDisabled(false);
      }
      else {
        setIsDisabled(true);
      }
  }, [email]);


  async function sendRecoveryPasswordEmail(e) {
      e.preventDefault();
      let message = '';
      if(!email) {            
          message += 'El campo del email está vacío.\n\n';
      }
      if(message.length !== 0) {
          //setIsLoading(false);
          toast.show(
              message,
              {
                  type: 'danger'
              }
          );
          //setVisibleModal(ModalType.Error, ModalTitle.ErrorTitle, message);
      }
      else {
        setIsLoading(true);
        const data = {
            email:email,
        }

        await axiosInstance.post('/sivaria/v1/email/sendRecoveryPasswordEmail', data)
        .then(function (response) {
            let message = 'Email enviado correctamente';
            //setVisibleModal(ModalType.Information, ModalTitle.InformationTitle, message);
            toast.show(
                message,
                {
                    type: 'success'
                }
            );

        })
        .catch(function (error) {
            setIsLoading(false);
            let message = 'Ha habido un error durante el proceso de registro del usuario. ' + error.response.data.data;
            //setVisibleModal(ModalType.Error, ModalTitle.ErrorTitle, message);
            //Alert.alert('Error', 'Error en el registro. Inténtelo de nuevo.')
            toast.show(
                message,
                {
                    type: 'danger'
                }
            );
        });
        setIsLoading(false);
      }
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
          <View style={{height: 200, alignItems: 'center', justifyContent: 'center'}}>
              <Text onPress={(e) => navigation.navigate('Login')} style={{color:'white', fontSize: 35, fontWeight: 'bold', textAlign: 'center'}}>SIVARIA</Text>
              <SivariaText fontSize={20}>Recuperación de contraseña</SivariaText>
          </View>
          
          <View style={{flex:1, backgroundColor: '#006E51', alignItems: 'center', justifyContent: 'center'}}>
              <View style={[stylesSivaria.whiteBoxContainer]}>
                    <View style={{height:500, width:'100%', alignItems:'center', justifyContent: 'center'}}>
                      <View style={{height:200, width:'100%',alignItems:'center', justifyContent: 'center'}}>
                        <View style={{width:'80%'}}>
                          <SivariaText color={'#006E51'} textAlign={'left'}>
                            Introduzca el email que usaste para registrarte, y te enviaremos un correo con un enlace para recuperar tu contraseña.
                          </SivariaText>
                          <SivariaText color={'#006E51'} textAlign={'left'}>
                            Si el correo no le ha llegado, pruebe a reenviar el correo dando al botón de nuevo.
                          </SivariaText>
                          <SivariaText color={'#006E51'} textAlign={'left'}>
                            Revise también si ha escrito su correo correctamente. 
                          </SivariaText>
                        </View>
                      </View>
                      <SivariaInput 
                          placeholder={'Email'}
                          value={email}
                          onChangeText={setEmail}
                          autoCorrect={false}
                          autoCapitalize={'none'} 
                          inputMode={'email'}
                      />
                    </View>
                  <View style={{height:80, width:'100%', alignItems:'center', justifyContent:'center'}}>
                      <SivariaButton onPress={sendRecoveryPasswordEmail} message={'ENVIAR CORREO'} disabled={isDisabled}/>
                  </View>
                  <View style={{height:80, width:'100%', alignItems:'center', justifyContent:'center'}}>
                    <SivariaText color={'grey'} isItalic={true}>
                      Por favor, ignore este email si no ha solicitado un cambio de contraseña.
                    </SivariaText>                  
                  </View>
              </View>
          </View>
      </Container>
    );
  };

export default ForgotPasswordScreen;