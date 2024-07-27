import { useEffect, useState } from 'react';
import { View, Text, Alert, SafeAreaView, Pressable, Modal } from 'react-native';
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
import { UserContext } from '../../context/user-context';
import ModalComponent from '../../components/modal-component';
import { AntDesign } from '@expo/vector-icons';
import { PrivacyPolicyModal } from '../privacy-policy-modal';
import { WelcomeMessageModal } from '../welcome-message-modal';

const HomeScreen = ({navigation}) => {
    const user = useContext(AuthContext);

    const userData = useContext(UserContext);

    const toast = useToast();

    const [isLoading, setIsLoading] = useState(false);

    const [isVisible, setModalVisible] = useState(false);
    const [modalTitle, setModalTitle] = useState('');
    const [modalType, setModalType] = useState('');
    const [modalMessage, setModalMessage] = useState('');

    const [isVisiblePrivacyModal, setIsVisiblePrivacyModal] = useState(false);
    const [isVisibleWelcomeModal, setIsVisibleWelcomeModal] = useState(false);
    /*
    async function sendPush(e) {
        e.preventDefault();
        setIsLoading(true);
        let data = {
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
        */

    function goToQuestionnaire(e) {
        //console.log(userData);
        if(userData.rolSlug == 'joven') {
            navigation.navigate('YoungstersQuestionnaireSivaria');
        }
        else if (userData.rolSlug == 'padre' || userData.rol == 'madre') {
            navigation.navigate('ParentsQuestionnaireSivaria');
        }
        else if (userData.rolSlug == 'profesional') {
            navigation.navigate('ProfessionalsQuestionnaireSivaria');
        }
    }

    if(isLoading) {
        return (
            <LoadingScreen />
        );
    }

    //<AntDesign name="infocirlce" size={24} color="black" />

    return (
      <>
        {/*
        <ModalComponent 
                animationType='slide'
                setIsVisible={setModalVisible}
                isVisible={isVisible}
                title={modalTitle}
                modalType={modalType}
                message={modalMessage}
        />
        */}
        {/*
        <View style={{flex:1, backgroundColor: 'white'}}>
            <View style={{flex:1, width: '100%', alignItems:'center', justifyContent: 'center'}}>
                <View style={{flex:1, width: '80%', alignItems: 'center', justifyContent: 'center'}}>
                    <SivariaButton onPress={(e) => sendPush(e)} message={'ENVIAR PUSH'} />
                </View>
            </View>
        </View>
        */}
        {/*<Modal
            animationType='slide'
            onRequestClose={() => setModalVisible(false)}
            visible={isVisible}
        >
            <View style={{alignItems:'center', justifyContent: 'center', flex:1}}>
                <View style={{height:200, backgroundColor: '#006E51', flexDirection:'row', width: '100%', borderBottomWidth: 2, borderBottomColor: 'grey', alignItems: 'center', justifyContent: 'center'}}>
                    <AntDesign name={'infocirlceo'} size={35} color="white" style={{paddingRight:10}}/>
                    <SivariaText fontSize={35}>INFORMACIÓN</SivariaText>
                </View>             
                <ScrollView style={{height:500, width:'100%', padding:10}}>
                    {isLoadingModal 
                    ? (<LoadingScreen />)
                    : 
                    (<>
                        <View>

                        </View>
                    </>)
                    }
                </ScrollView>
                <View style={{height:200, width:'100%', alignItems:'center', justifyContent: 'center', borderTopWidth:2, borderTopColor: 'grey'}}>
                    <SivariaButton onPress={() => setIsVisible(false)}>
                        <SivariaText isBold={true}>
                            CERRAR
                        </SivariaText>
                    </SivariaButton>
                </View>
            </View>
        </Modal>
        */}
        <PrivacyPolicyModal isVisible={isVisiblePrivacyModal} setModalVisible={setIsVisiblePrivacyModal} />
        <WelcomeMessageModal isVisible={isVisibleWelcomeModal} setModalVisible={setIsVisibleWelcomeModal} />
        <View style={{height: 1000, backgroundColor: 'white'}}>
            
            <View style={{height: 100, alignItems: 'center', justifyContent: 'center'}}>
                <View style={{flex:1, width:'80%', alignItems: 'center', justifyContent: 'flex-end',  flexDirection:'row'}}>
                    <View style={{width:80}}>
                        <SivariaButton 
                            onPress={() => setIsVisibleWelcomeModal(true)} 
                            disabled={false} 
                            message={
                                <AntDesign
                                    name={'question'} 
                                    size={20} 
                                    color="white" 
                                />
                            }
                        />
                    </View>
                    <View style={{width:80}}>
                        <SivariaButton 
                            onPress={() => setIsVisiblePrivacyModal(true)} 
                            disabled={false} 
                            message={
                                <AntDesign
                                    name={'filetext1'} 
                                    size={20} 
                                    color="white" 
                                />
                            }
                        />
                    </View>
                </View>
                {/*
                <Pressable   
                    style={[
                            ({pressed}) => [
                                {
                                    backgroundColor: pressed ? '#7bdcb5' : '#006E51',
                                    borderColor: pressed ? '#7bdcb5' : '#024332',
                                },
                            ],
                            {
                                flex:1,
                                borderRadius: 8,
                            },
                        ]}
                        onPress={() => console.log('INFO POLÍTICA')}
                    >
                        <AntDesign
                            name={'infocircle'} 
                            size={20} 
                            color="black" 
                            //style={{paddingRight:10}}
                        />
                </Pressable>
                */}
                {/*
                <Pressable   
                    style={[
                            ({pressed}) => [
                                {
                                    backgroundColor: pressed ? '#7bdcb5' : '#006E51',
                                    borderColor: pressed ? '#7bdcb5' : '#024332',
                                },
                            ],
                            {
                                flex:1,
                                borderRadius: 8,
                            },
                        ]}
                        onPress={() => console.log('INFO TUTORIAL')}
                    >
                        <AntDesign
                            name={'filetext1'} 
                            size={20} 
                            color="black" 
                        />
                </Pressable>
                */}
            </View>
            <View style={{height:200, alignItems:'center', justifyContent: 'center'}}>
                <SivariaButton onPress={(e) => goToQuestionnaire(e)} message={'COMENZAR CUESTIONARIO'} />
            </View>
        </View>
      </>
  );
}
  
export default HomeScreen;