import { useEffect, useState, useCallback } from 'react';
import { View, Text, Alert, SafeAreaView, Pressable, ScrollView, RefreshControl } from 'react-native';
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
import { DataTable } from 'react-native-paper';

import { Modal } from 'react-native';
//import YoungFormTemplate from './form-templates/young-form-template/young-form-template';
//import FamilyFormTemplate from './form-templates/family-form-template/family-form-template';
//import ProfessionalFormTemplate from './form-templates/professional-form-template/professional-form-template';
import { FormTemplate } from './form-templates/form-template';
import CollapsibleView, { AccordionList } from '../../components/collapsible-view';

const PatientsScreen = ({navigation}) => {
    const user = useContext(AuthContext);

    const userData = useContext(UserContext);

    const toast = useToast();

    const [isLoading, setIsLoading] = useState(false);
    const [isLoadingModal, setIsLoadingModal] = useState(false);

    const [isVisible, setModalVisible] = useState(false);
    const [modalTitle, setModalTitle] = useState('');
    const [modalType, setModalType] = useState('');
    const [modalMessage, setModalMessage] = useState('');

    const [formInfo, setFormInfo] = useState({});
    const [isData, setIsData] = useState(false);

    const [families, setFamilies] = useState([]);
    const [refreshing, setRefreshing] = useState(false);
    
    async function loadFamilies() {
        setIsLoading(true);

        data = {
            email: await getItemLocalStorage('email'),
        }

        axiosInstance.post("/sivaria/v1/user/getFamilies", data)
        .then(function (response) {
            //console.log(response.data.data);
            setFamilies(response.data.data);
        })
        .catch(function (error) {
            let message = 'Error cargando los registros de los cuestionarios';
            //setVisibleModal(ModalType.Esrror, ModalTitle.ErrorTitle, message);
            toast.show(
                message,
                {
                    type: 'danger'
                }
            );
        });
        setIsLoading(false);
    }
    /*
    async function loadFormInfo(e, form_code) {
        e.preventDefault();
        setIsLoading(true);
        let data = {
            email: await getItemLocalStorage('email'),
            code: form_code,
        };

        axiosInstance.post("/sivaria/v1/forms/getFormInfo", data)
        .then(function (response) {
            console.log(response.data.data);
            setFormInfo(response.data.data);
            setIsData(true);
            setModalVisible(true);
        })
        .catch(function (error) {
            let message = 'Error cargando la infromación del cuestionario ' + form_code;
            //setVisibleModal(ModalType.Esrror, ModalTitle.ErrorTitle, message);
            toast.show(
                message,
                {
                    type: 'danger'
                }
            );
        });
        setIsLoading(false);
    }*/

    const onRefresh = useCallback(() => {
        setRefreshing(true);
        setTimeout(() => {
            loadFamilies();
            setRefreshing(false);
        }, 2000);
    }, []);
    
    useEffect(() => {
        loadFamilies();
    }, []);
    /*
    const data = [
        {
            id: 5,
            title: "Tomás Ramírez (TR24072009)",
            content: {
            parent_1: "-",
            parent_2: "Aldair Maldonado Padre - aldairfm@ucm.es",
            responsible: "Aldair Maldonado Profesional - ranking123@hotmail.es"
            }
        },
        {
            id: 6,
            title: "Tomás Ramírez 2 (TR24072009)",
            content: {
            parent_1: "-",
            parent_2: "Aldair Maldonado Padre 2 - aldairfm@ucm.es",
            responsible: "Aldair Maldonado Profesional 2 - ranking123@hotmail.es"
            }
        },
        {
            id: 7,
            title: "Tomás Ramírez 2 (TR24072009)",
            content: {
            parent_1: "-",
            parent_2: "Aldair Maldonado Padre 2 - aldairfm@ucm.es",
            responsible: "Aldair Maldonado Profesional 2 - ranking123@hotmail.es"
            }
        },
        {
            id: 8,
            title: "Tomás Ramírez 2 (TR24072009)",
            content: {
            parent_1: "-",
            parent_2: "Aldair Maldonado Padre 2 - aldairfm@ucm.es",
            responsible: "Aldair Maldonado Profesional 2 - ranking123@hotmail.es"
            }
        },
        {
            id: 9,
            title: "Tomás Ramírez 2 (TR24072009)",
            content: {
            parent_1: "-",
            parent_2: "Aldair Maldonado Padre 2 - aldairfm@ucm.es",
            responsible: "Aldair Maldonado Profesional 2 - ranking123@hotmail.es"
            }
        },
        {
            id: 23,
            title: "Tomás Ramírez 2 (TR24072009)",
            content: {
            parent_1: "-",
            parent_2: "Aldair Maldonado Padre 2 - aldairfm@ucm.es",
            responsible: "Aldair Maldonado Profesional 2 - ranking123@hotmail.es"
            }
        },
        {
            id: 22,
            title: "Tomás Ramírez 2 (TR24072009)",
            content: {
            parent_1: "-",
            parent_2: "Aldair Maldonado Padre 2 - aldairfm@ucm.es",
            responsible: "Aldair Maldonado Profesional 2 - ranking123@hotmail.es"
            }
        },
        {
            id: 21,
            title: "Tomás Ramírez 2 (TR24072009)",
            content: {
            parent_1: "-",
            parent_2: "Aldair Maldonado Padre 2 - aldairfm@ucm.es",
            responsible: "Aldair Maldonado Profesional 2 - ranking123@hotmail.es"
            }
        },
        {
            id: 20,
            title: "Tomás Ramírez 2 (TR24072009)",
            content: {
            parent_1: "-",
            parent_2: "Aldair Maldonado Padre 2 - aldairfm@ucm.es",
            responsible: "Aldair Maldonado Profesional 2 - ranking123@hotmail.es"
            }
        },
        {
            id: 10,
            title: "Tomás Ramírez 2 (TR24072009)",
            content: {
            parent_1: "-",
            parent_2: "Aldair Maldonado Padre 2 - aldairfm@ucm.es",
            responsible: "Aldair Maldonado Profesional 2 - ranking123@hotmail.es"
            }
        },
        {
            id: 11,
            title: "Tomás Ramírez 2 (TR24072009)",
            content: {
            parent_1: "-",
            parent_2: "Aldair Maldonado Padre 2 - aldairfm@ucm.es",
            responsible: "Aldair Maldonado Profesional 2 - ranking123@hotmail.es"
            }
        },
        {
            id: 12,
            title: "Tomás Ramírez 2 (TR24072009)",
            content: {
            parent_1: "-",
            parent_2: "Aldair Maldonado Padre 2 - aldairfm@ucm.es",
            responsible: "Aldair Maldonado Profesional 2 - ranking123@hotmail.es"
            }
        },
        {
            id: 13,
            title: "Tomás Ramírez 2 (TR24072009)",
            content: {
            parent_1: "-",
            parent_2: "Aldair Maldonado Padre 2 - aldairfm@ucm.es",
            responsible: "Aldair Maldonado Profesional 2 - ranking123@hotmail.es"
            }
        },
        {
            id: 56,
            title: "Tomás Ramírez 2 (TR24072009)",
            content: {
            parent_1: "-",
            parent_2: "Aldair Maldonado Padre 2 - aldairfm@ucm.es",
            responsible: "Aldair Maldonado Profesional 2 - ranking123@hotmail.es"
            }
        }
    ];*/

    if(isLoading) {
        return (
            <LoadingScreen />
        );
    }

    return (
      <>
        <Modal
            animationType='slide'
            onRequestClose={() => setModalVisible(false)}
            visible={isVisible}
        >
            <View style={{alignItems:'center', justifyContent: 'center', flex:1}}>
                <View style={{height:100, backgroundColor: '#006E51', flexDirection:'row', width: '100%', borderBottomWidth: 2, borderBottomColor: 'grey', alignItems: 'center', justifyContent: 'center'}}>
                    <AntDesign name={'infocirlceo'} size={35} color="white" style={{paddingRight:10}}/>
                    <SivariaText fontSize={35}>INFORMACIÓN</SivariaText>
                </View>             
                <ScrollView style={{height:500, width:'100%', padding:10}}>
                    <FormTemplate isData={isData} formData={formInfo}/>
                </ScrollView>
                <View style={{height:100, width:'100%', alignItems:'center', justifyContent: 'center', borderTopWidth:2, borderTopColor: 'grey'}}>
                    <View style={{flex:1, width: '100%', alignItems: 'center', justifyContent: 'center'}}>
                        <Pressable 
                        style={
                            ({pressed}) => [
                                {
                                    backgroundColor: pressed ? '#7bdcb5' : '#006E51',
                                    borderColor: pressed ? '#7bdcb5' : '#024332',
                                },
                                {
                                    flex:1, 
                                    width: '100%', 
                                    alignItems: 'center', 
                                    justifyContent: 'center',
                                },
                            ]
                        } 
                            onPress={() => setModalVisible(false)}>
                            <Text style={{color: 'white', fontWeight: 'bold'}}>
                                CERRAR
                            </Text>
                        </Pressable>
                    </View>
                </View>
            </View>
        </Modal>
        
        <ScrollView 
            style={{flex:1}}
            refreshControl={
                <RefreshControl refreshing={refreshing} onRefresh={onRefresh} />
            }
        >
            <AccordionList data={families}/>
        </ScrollView>
      </>
  );
}
  
export default PatientsScreen;