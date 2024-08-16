import React, { useContext, useEffect, useState, useCallback, useRef } from 'react';
import { StyleSheet, ActivityIndicator, ScrollView, SafeAreaView, View, Text, TextInput, Pressable, Alert, RefreshControl, Animated } from 'react-native';
import Dropdown from '../../components/dropdown';
import ShowHidePasswordInput from '../../components/show-hide-password-input';
import stylesSivaria from '../../styles/styles-sivaria';
import PhoneInput from "react-native-phone-input";
import LoadingScreen from '../loading-screen';

import { getItemLocalStorage, removeItemLocalStorage, setItemLocalStorage } from '../../utils/general-local-storage';
import { ModalType, ModalTitle } from '../../utils/enum-types-modal';

import Container from '../../components/component-containers/container';
import axiosInstance from '../../utils/axios-config-web';

import ModalComponent from '../../components/modal-component';

import SivariaText from '../../components/sivaria-text';
import SivariaButton from '../../components/sivaria-button';
import { AuthContext } from '../../context/auth-context';

import useModal from '../../utils/modal-hook';
import { useToast } from 'react-native-toast-notifications';
import { UserContext } from '../../context/user-context';

import useUserData from '../../utils/user-user-data-hook';
import { AntDesign } from '@expo/vector-icons';
import DynamicHeader from '../../components/dynamic-header';


const ProfileScreen = ({navigation}) => {
    const user = useContext(AuthContext);
    const userApp = useContext(UserContext);

    const [isLoading, setIsLoading] = useState(true);

    const { modalType, modalTitle, modalMessage, isVisible, setModalVisible, setVisibleModal } = useModal();

    const [userData, setUserData] = useState([]);

    const toast = useToast();

    const { updateUserStateVariables, removeUserStateVariables } = useUserData();

    const [refreshing, setRefreshing] = useState(false);

    /* DynamicHeader variables */
    const scrollOffsetY = useRef(new Animated.Value(0)).current;

    async function fetchUserData() {
        //console.log(userApp);
        setIsLoading(true);
        let email = await getItemLocalStorage('email');
        await axiosInstance.get("/sivaria/v1/user/getUserByEmail/"+email)
        .then(async function (response) {
            data = response.data.data;
            //console.log(data);
            newData = {};
            data.map((element) => {
                newData[element.key] = element.value;
            });

            // Update local storage and state variables.
            await setItemLocalStorage('email', newData['email']);
            await setItemLocalStorage('firstName', newData['first_name']);
            await setItemLocalStorage('lastName', newData['last_name']);
            await setItemLocalStorage('phoneNumber', newData['phone']);
            //console.log(newData);
            let rolDescription = (newData['rol_description']) ? newData['rol_description'] : null;
            await setItemLocalStorage('rol', rolDescription);  
            let rolSlug = (rolDescription) ? rolDescription.toLowerCase() : null;
            await setItemLocalStorage('rolSlug', rolSlug ?? ''); 
            if(rolSlug === 'joven') {    
                await setItemLocalStorage('emailParent1', newData['email_parent_1'] ?? '');
                await setItemLocalStorage('emailParent2', newData['email_parent_2'] ?? '');
            }
            
            setUserData(response.data.data);
            setIsLoading(false);
            //console.log(response.data.data);
        })
        .catch(function (error) {         
            setIsLoading(false);
            let message = 'Ha habido un error obteniendo los datos del usuario.';
            toast.show(
                message,
                {
                    type: 'danger'
                }
            );
            //setVisibleModal(ModalType.Error, ModalTitle.ErrorTitle, message);
        });
        /*       
        let data = [
            {
                title: "Nombre",
                value: userApp.firstName ?? '',
                key: "first_name"
            },
            {
                title: "Apellidos",
                value: userApp.lastName ?? '',
                key: "last_name"
            },
            {
                title: "Email",
                value: userApp.email ?? '',
                key: "email"
            },
            {
                title: "Teléfono",
                value: userApp.phone ?? '',
                key: "phone"
            },
            {
                title: "Rol",
                value: userApp.rol ?? '',
                key: "rol_description"
            }
        ]
        if(userApp.rolSlug === 'joven') {
            let extraData = [
                {
                    title: "Email madre o figura parental 1",
                    value: userApp.emailParent1 ?? '',
                    key: "email_parent_1"
                },
                {
                    title: "Email padre o figura parental 1",
                    value: userApp.emailParent2 ?? '',
                    key: "email_parent_2"
                }
            ];
            data = [...data, extraData];
        }
        //console.log(data);
        setUserData(data);
        setIsLoading(false);
        */
    }

    const onRefresh = useCallback(() => {
        setRefreshing(true);
        setTimeout(() => {
            fetchUserData();
            setRefreshing(false);
        }, 2000);
      }, []);

    useEffect(() => {
        fetchUserData();
    }, []);

    async function callLogout(e) {
        e.preventDefault();
        setIsLoading(true);
        await axiosInstance.post("/sivaria/v1/user/logout")
        .then(async function (response) {
            await removeItemLocalStorage('userToken');
            await removeItemLocalStorage('email');
            // Remove local storage and user state variables
            await removeItemLocalStorage('userId');
            await removeItemLocalStorage('firstName');
            await removeItemLocalStorage('lastName');
            await removeItemLocalStorage('phoneNumber');
            await removeItemLocalStorage('rol');
            //let rolSlug = (newData['rol_description']) ? newData['rol_description'].toLowerCase() : null;
            await removeItemLocalStorage('rolSlug');
            //if(rolSlug === 'joven') {    
                await removeItemLocalStorage('emailParent1');
                await removeItemLocalStorage('emailParent2');
            //}

            user.setIsAuthenticated(false);

            toast.show(
                'Sesión cerrada exitosamente',
                {
                    type: 'success'
                }
            );
            setIsLoading(false);
            //user.logout();
            //removeUserStateVariables();
        })
        .catch(function (error) {
            setIsLoading(false);
            toast.show(
                'Error en el cierre de sesión del usuario',
                {
                    type: 'danger'
                }
            );
        });
    }

    async function callDeleteAccount(e) {
        e.preventDefault();
        setIsLoading(true);
        email = await getItemLocalStorage('email');
        await axiosInstance.delete("/sivaria/v1/user/email/" + email)
        .then(async function (response) {
            //console.log('Cuenta eliminada correctamente');
            toast.show(
                'Cuenta eliminada exitosamente',
                {
                    type: 'success'
                }
            );
            removeItemLocalStorage('email');
            removeItemLocalStorage('userToken');
            setIsLoading(false);
            user.logout(false);
        })
        .catch(function (error) {
            setIsLoading(false);
            let message = 'Ha habido un error eliminando la cuenta del usuario.';
            //setVisibleModal(ModalType.Error, ModalTitle.ErrorTitle, message);
            toast.show(
                message,
                {
                    type:'danger'
                }
            );
        });
    }
    
    if(isLoading) {
        return (
            <LoadingScreen />
        );
    }

    return (
        <>
            <ModalComponent 
                animationType='slide'
                setIsVisible={setModalVisible}
                isVisible={isVisible}
                title={modalTitle}
                modalType={modalType}
                message={modalMessage}
            />
            
            {/*
            <View style={{flex:1, width:'90%', alignItems: 'flex-end' , justifyContent:'center'}}>
                <Pressable 
                    onPress={() => fetchUserData()}
                >
                    <AntDesign 
                        name={'reload1'} 
                        size={20} 
                        color={'white'} 
                    />
                </Pressable>
            </View>
            */}
            {/*
            <View style={{height: 100, flexDirection: 'center', alignItems: 'center', justifyContent: 'center', backgroundColor: '#006E51'}}>
                <View style={{flex:1, width:'100%', alignItems: 'center', justifyContent: 'center', borderBottomWidth: 2, borderBottomColor: '#024332'}}>
                    <Text style={{fontSize: 25, color:'white', fontWeight:'bold'}}>
                        DATOS DEL USUARIO
                    </Text>
                </View>
            </View>
            */}
            {/*<DynamicHeader animHeaderValue={scrollOffsetY}>
                <Text style={{fontSize: 25, color:'white', fontWeight: 'bold'}}>
                    DATOS DEL USUARIO
                </Text>
            </DynamicHeader>
            */}
            <ScrollView
                scrollEventThrottle={16}
                onScroll={Animated.event(
                    [{ nativeEvent: { contentOffset: { y: scrollOffsetY}}}],
                    {useNativeDriver: false}
                )} 
                style={{backgroundColor: 'white', borderBottomWidth: 2, borderColor: 'grey'}}
                refreshControl={
                    <RefreshControl refreshing={refreshing} onRefresh={onRefresh}/>
                }
            >
                {
                    userData.map((data, index) => {
                            return (
                                <View key={data.key} style={{height: 100, flexDirection: 'row', borderWidth: 2, borderColor: 'grey'}}>
                                    {/*console.log(data)*/}
                                    <View key={'title_'+index} style={{flex:1, alignItems:'center', justifyContent: 'center'}}>
                                        <SivariaText color={'black'} fontSize={15} isBold={true}>{data.title}</SivariaText>
                                    </View>
                                    <View key={'value_'+index} style={{flex:2, alignItems: 'center', justifyContent: 'center', backgroundColor:'#ececec', padding:10}}>
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
            </ScrollView>
            {/*<Text>PROFILE SCREEN</Text>*/}
            <View style={{height: 100, flexDirection: 'row', backgroundColor: 'white'}}>
                    <View style={{flex:1, alignItems: 'center', justifyContent: 'center'}}>
                        <View style={{flex:1, width:'80%', alignItems: 'center', justifyContent: 'center'}}>
                            <SivariaButton onPress={(e) => callLogout(e)} message={'CERRAR SESIÓN'}/>
                        </View>
                    </View>
                    <View style={{flex:1, alignItems: 'center', justifyContent: 'center'}}>
                        <View style={{flex:1, width:'80%', alignItems: 'center', justifyContent: 'center'}}>
                            <SivariaButton onPress={(e) => navigation.navigate('EditData')} message={'EDITAR DATOS'}/>
                        </View>
                    </View>
                    <View style={{flex:1, alignItems: 'center', justifyContent: 'center'}}>
                        <View style={{flex:1, width:'80%', alignItems: 'center', justifyContent: 'center'}}>
                            <SivariaButton onPress={(e) => callDeleteAccount(e)} message={'ELIMINAR CUENTA'}/>
                        </View>
                    </View>
                </View>
        </>
    );
}

export default ProfileScreen;