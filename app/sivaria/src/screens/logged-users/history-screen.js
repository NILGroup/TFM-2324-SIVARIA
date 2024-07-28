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

const HistoryScreen = ({navigation}) => {
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

    const [items, setItems] = useState([]);
    const [refreshing, setRefreshing] = useState(false);

    const [page, setPage] = useState(0);
    const [numberOfItemsPerPageList] = useState([5, 10, 20]);
    const [itemsPerPage, onItemsPerPageChange] = useState(
        numberOfItemsPerPageList[0]
    );

    const from = page * itemsPerPage;
    const to = Math.min((page + 1) * itemsPerPage, items.length);

    async function loadItems() {
        setIsLoading(true);
        let data = {
            email: await getItemLocalStorage('email'),
        };
        
        axiosInstance.post("/sivaria/v1/forms/getFormsDT", data)
        .then(function (response) {
            //console.log(response.data.data);
            setItems(response.data.data);
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
    }

    const onRefresh = useCallback(() => {
        setRefreshing(true);
        setTimeout(() => {
            loadItems();
          setRefreshing(false);
        }, 2000);
      }, []);
    
    useEffect(() => {
        loadItems();
    }, []);

    useEffect(() => {
        setPage(0);
    }, [itemsPerPage]);

    if(isLoading) {
        return (
            <LoadingScreen />
        );
    }

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
            <DataTable>
            <DataTable.Header>
                <DataTable.Title>Código</DataTable.Title>
                <DataTable.Title>Hecho por</DataTable.Title>
                <DataTable.Title>Paciente</DataTable.Title>
                <DataTable.Title>Rol</DataTable.Title>
                <DataTable.Title>Fecha y Hora</DataTable.Title>
                <DataTable.Title>Resultado</DataTable.Title>
            </DataTable.Header>

            {items.slice(from, to).map((item) => (
                <DataTable.Row key={item.code} onPress={(e) => loadFormInfo(e,item.code)}>
                    <DataTable.Cell>{item.code}</DataTable.Cell>
                    <DataTable.Cell>{item.user}</DataTable.Cell>
                    <DataTable.Cell>{item.to_user}</DataTable.Cell>
                    <DataTable.Cell>{item.rol}</DataTable.Cell>
                    <DataTable.Cell>{item.datetime_str}</DataTable.Cell>
                    <DataTable.Cell>{item.result}</DataTable.Cell>
                </DataTable.Row>
            ))}

            <DataTable.Pagination
                page={page}
                numberOfPages={Math.ceil(items.length / itemsPerPage)}
                onPageChange={(page) => setPage(page)}
                label={`${from + 1}-${to} de ${items.length}`}
                numberOfItemsPerPageList={numberOfItemsPerPageList}
                numberOfItemsPerPage={itemsPerPage}
                onItemsPerPageChange={onItemsPerPageChange}
                showFastPaginationControls
                selectPageDropdownLabel={'Filas por página'}
            />
            </DataTable>
        </ScrollView>
      </>
  );
}
  
export default HistoryScreen;