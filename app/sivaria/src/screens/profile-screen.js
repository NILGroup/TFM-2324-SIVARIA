import React, { useEffect, useState } from 'react';
import { StyleSheet, ActivityIndicator, ScrollView, SafeAreaView, View, Text, TextInput, Pressable, Alert } from 'react-native';
import Dropdown from '../components/sivaria-custom-basic-components/dropdown';
import ShowHidePasswordInput from '../components/show-hide-password-input';
import stylesSivaria from '../styles/styles-sivaria';
import PhoneInput from "react-native-phone-input";
import LoadingScreen from './loading-screen';

import { getItemLocalStorage } from '../utils/general-local-storage';
import { ModalType, ModalTitle } from '../utils/enum-types-modal';

import Container from '../components/component-containers/container';
import axiosInstance from '../utils/axios-config-web';

import ModalComponent from '../components/modal-component';

import SivariaText from '../components/sivaria-custom-basic-components/sivaria-text';
import SivariaButton from '../components/sivaria-custom-basic-components/sivaria-button';

const ProfileScreen = ({navigation}) => {
    const [isLoadingUserData, setIsLoadingUserData] = useState(true);

    const [modalType, setModalType] = useState('');
    const [modalTitle, setModalTitle] = useState('');
    const [modalMessage, setModalMessage] = useState('');
    const [isVisible, setModalVisible] = useState(false);

    const [userData, setUserData] = useState([]);

    useEffect(() => {
        async function fetchUserData() {
            let email = await getItemLocalStorage('email');
            await axiosInstance.get("/sivaria/v1/user/getUserByEmail/"+email)
            .then(async function (response) {
                //console.log(response);
                /*user = response.data.data;
                let data = {
                    'Nombre': user.first_name,
                    'Apellidos': user.last_name, 
                    'Email': user.email,
                    'Teléfono': user.first_name,
                    'Rol': user.first_name,
                }
                if ('email_parent_1' in user) {
                    data['emailParent1'] = user.email_parent_1 ?? null);
                }
                if ('email_parent_1' in user) {
                    data['Tel'] = user.email_parent_1 ?? null);
                }
                    */
                setUserData(response.data.data);
                setIsLoadingUserData(false);
            })
            .catch(function (error) {         
                const message = 'Ha habido un error obteniendo los datos del usuario.';
                setVisibleModal(ModalType.Error, ModalTitle.ErrorTitle, message);
            });

        }

        fetchUserData();
    }, []);

    function setVisibleModal(modalType, title, message) {
        setModalType(modalType)
        setModalTitle(title);
        setModalMessage(message);
        setModalVisible(true);
    }

    if(isLoadingUserData) {
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
            <View style={{flex:1, backgroundColor: 'white'}}>
                {
                    userData.map((data, index) => {
                            return (
                                <View key={data.key} style={{flex:1, flexDirection: 'row', borderWidth: 2, borderColor: 'grey'}}>
                                    {/*console.log(data)*/}
                                    <View key={'title_'+index} style={{flex:1, alignItems:'center', justifyContent: 'center'}}>
                                        <SivariaText color={'black'} fontSize={15}>{data.title}</SivariaText>
                                    </View>
                                    <View key={'value_'+index} style={{flex:1, alignItems: 'flex-start', justifyContent: 'center'}}>
                                        <SivariaText color={'black'} fontSize={15}>
                                            {
                                                (data.value !== null && data.value !== '') ? data.value : 'Ninguno'
                                            }
                                        </SivariaText>
                                    </View>
                                </View>
                            );
                        }
                    )
                }
                {/*<Text>PROFILE SCREEN</Text>*/}
                <View style={{flex:1, flexDirection: 'row', backgroundColor: 'green'}}>
                    <View style={{flex:1, alignItems: 'center', justifyContent: 'center', backgroundColor: 'red'}}>
                        <View style={{flex:1, width:'80%', alignItems: 'center', justifyContent: 'center', backgroundColor: 'blue'}}>
                            <SivariaButton onPress={(e) => callLogout(e)}>
                                <SivariaText isBold={true}>
                                    CERRAR SESIÓN
                                </SivariaText>
                            </SivariaButton>
                        </View>
                    </View>
                    <View style={{flex:1, alignItems: 'center', justifyContent: 'center'}}>
                        <View style={{flex:1, width:'80%', alignItems: 'center', justifyContent: 'center'}}>
                            <SivariaButton onPress={(e) => callLogout(e)}>
                                <SivariaText isBold={true}>
                                    ELIMINAR CUENTA
                                </SivariaText>
                            </SivariaButton>
                        </View>
                    </View>
                </View>
            </View>
        </Container>
    );
}

export default ProfileScreen;