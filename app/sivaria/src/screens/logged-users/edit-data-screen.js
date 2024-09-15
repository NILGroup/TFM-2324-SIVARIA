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
import SivariaInput from '../../components/sivaria-input';
import SivariaSpanishPhoneInput from '../../components/sivaria-spanish-phone-input';
import { UserContext } from '../../context/user-context';

import { setItemLocalStorage } from '../../utils/general-local-storage';

import ShowHidePasswordInput from '../../components/show-hide-password-input';

const EditDataScreen = ({navigation, props}) => {
    const user = useContext(AuthContext);
    const userApp = useContext(UserContext);

    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [phoneNumber, setPhoneNumber] = useState('');
    const [rol, setRol] = useState('');
    const [emailParent1, setEmailParent1] = useState('');
    const [emailParent2, setEmailParent2] = useState('');

    const toast = useToast();

    const [isLoading, setIsLoading] = useState(false);

    const [isDisabled, setIsDisabled] = useState(true);

    async function callEditUserData(e) {
        e.preventDefault();

        let message = '';
        if(!firstName && !lastName && !phoneNumber) {
            message += 'Todos los campos están vacíos. Rellena alguna para enviar el formulario\n\n';
        }
        if(phoneNumber && isNaN(phoneNumber)) {
            message += 'El número de teléfono introducido no es numérico.\n\n';
        }
        if(password && !confirmPassword) {
            message += 'Se ha rellenado el campo de contraseña, pero el campo de confirmación de contraseña está vacío.\n\n';
        }
        if(!password && confirmPassword) {
            message += 'Se ha rellenado el campo de confirmación de contraseña, pero el campo de contraseña está vacío.\n\n';
        }
        if(password && confirmPassword && (password !== confirmPassword)) {
            message += 'Ambos campos de contraseñas no coinciden.\n\n';
        }

        if(message.length !== 0) {
            //setIsLoading(false);
            toast.show(message,{type: 'danger'});
            //setVisibleModal(ModalType.Error, ModalTitle.ErrorTitle, message);
        }
        else {
            setIsLoading(true);
            email = await getItemLocalStorage('email');
            let data = {};
            if (firstName) {
                data['first_name'] = firstName;
            }
            if (lastName) {
                data['last_name'] = lastName;
            }
            if (phoneNumber) {
                data['phone'] = phoneNumber;
            }
            //console.log(data);
            await axiosInstance.put("/sivaria/v1/user/email/" + email, data)
            .then(async function (response) {
                //console.log(response);
                //console.log('Cuenta eliminada correctamente');
                //let rolDescription = (userData.rol) ? userData.rol.description : null;
                //await setItemLocalStorage('rol', rolDescription);  
                //let rolSlug = (userData.rol) ? userData.rol.slug : null;
                //await setItemLocalStorage('rolSlug', rolSlug); 
                //if(rolSlug === 'joven') {
                    //await setItemLocalStorage('emailParent1', userData.email_parent_1); 
                    //await setItemLocalStorage('emailParent2', userData.email_parent_2); 
                //}

                if (firstName) {
                    await setItemLocalStorage('firstName', data['first_name']);   
                    userApp.setFirstName(firstName);
                }
                if (lastName) {
                    await setItemLocalStorage('lastName', data['last_name']);   
                    userApp.setLastName(lastName);
                }
                if (phoneNumber) {
                    await setItemLocalStorage('phoneNumber', data['phone']);
                    userApp.setPhoneNumber(phoneNumber);
                }
                if ((password && confirmPassword && password === confirmPassword)) {
                    await setItemLocalStorage('phoneNumber', data['phone']);
                    userApp.setPhoneNumber(phoneNumber);
                }
                setIsLoading(false);
                toast.show(
                    'Datos actualizados correctamente.\nActualiza la página del perfil para obtener los nuevos datos de tu usuario.',
                    {
                        type: 'success'
                    }
                );
                navigation.navigate('Profile');
            })
            .catch(function (error) {
                setIsLoading(false);
                let message = 'Ha habido un error actualizando los datos del usuario.';
                //setVisibleModal(ModalType.Error, ModalTitle.ErrorTitle, message);
                toast.show(
                    message,
                    {
                        type:'danger'
                    }
                );
            });
        }
    }

    useEffect(() => {
        function enableEditButton(){
            if(firstName || lastName || phoneNumber || (password && confirmPassword)) {
                setIsDisabled(false);
            }
            else {
                setIsDisabled(true);
            }
        }
        enableEditButton();
    }, [firstName, lastName, phoneNumber, password, confirmPassword]);

    if(isLoading) {
        return (
            <LoadingScreen />
        );
    }

    return (
      <Container>
        <View style={{flex:2, backgroundColor: '#006E51'}}>
            <View style={{flex:1, width: '100%', alignItems:'center', justifyContent: 'center'}}>
                <View style={{flex:1, width: '80%', alignItems:'center', justifyContent: 'center'}}>
                        <ShowHidePasswordInput 
                            placeholder='Contraseña' 
                            password={password} 
                            onChangeText={setPassword} />
                    </View>
                    <View style={{flex:1, width: '80%', alignItems:'center', justifyContent: 'center'}}>
                        <ShowHidePasswordInput 
                            placeholder='Repetir Contraseña' 
                            password={confirmPassword} 
                            onChangeText={setConfirmPassword} />
                    </View>
                <View style={{flex:1, width: '80%', alignItems: 'center', justifyContent: 'center'}}>
                    <SivariaSpanishPhoneInput 
                            placeholder={'Número de teléfono'}
                            phoneNumber={phoneNumber}
                            onChangeText={setPhoneNumber}
                    />
                </View>
                
                <View style={[stylesSivaria.whiteBoxContainer, {alignItems:'center', justifyContent: 'center'}]}>
                    <View style={{flex:1, width:'80%', alignItems: 'center', justifyContent: 'center'}}>
                        <SivariaButton onPress={(e) => callEditUserData(e)} message={'ENVIAR'} disabled={isDisabled}/>
                    </View>
                    <View style={{flex:1, width:'80%', alignItems: 'center', justifyContent: 'center'}}>
                        <SivariaButton onPress={() => navigation.navigate('Profile')} message={'VOLVER'}/>
                    </View>
                </View>
            </View>
        </View>
      </Container>
  );
}
  
export default EditDataScreen;