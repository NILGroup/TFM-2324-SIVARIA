import { Modal, Pressable, Text, View, StyleSheet, ScrollView } from "react-native";
import stylesSivaria from "../styles/styles-sivaria";
import stylesSivariaModal from "../styles/styles-sivaria-modal";
import SivariaButton from "./sivaria-custom-basic-components/sivaria-button";
import SivariaText from "./sivaria-custom-basic-components/sivaria-text";
import { AntDesign } from "@expo/vector-icons";
import { ModalIcon, ModalType, ModalBackgroundColor } from "../utils/enum-types-modal";
import { useState } from "react";

const ModalComponent = ({animationType, setIsVisible, isVisible, modalType, title, message}) => {

    function getModalIcon() {
        switch(modalType) {
            case ModalType.Error:
                return ModalIcon.ErrorIcon;
            case ModalType.Information:
                return ModalIcon.InformationIcon;
            default:
                return '';       
        }
    }

    function getBackgroundColor() {
        switch(modalType) {
            case ModalType.Error:
                return ModalBackgroundColor.ErrorBackgroundColor;
            case ModalType.Information:
                return ModalBackgroundColor.InformationBackgroundColor;
            default:
                return 'white';        
        }
    }

    const modalIcon = getModalIcon();
    const backgroundColor = getBackgroundColor();

    return(
        /*
        <Modal animationType={animationType}
                onRequestClose={() => setIsVisible(false)}
                visible={isVisible}
        >
            <View style={styles.container}>
                <Text styles={styles.titleText}>{title}</Text>
                <Text>{message}</Text>
                <Br />
                <Pressable onPress={() => setIsVisible(false)}>
                    <Text>Cerrar</Text>
                </Pressable>            
            </View>

        </Modal>
        */
        <Modal animationType={animationType}
                onRequestClose={() => setIsVisible(false)}
                visible={isVisible}
        >
            <View style={styles.modalContainer}>
                <View style={{backgroundColor:backgroundColor, flex:0.5, flexDirection:'row', width: '100%', borderBottomWidth: 2, borderBottomColor: 'grey', alignItems: 'center', justifyContent: 'center'}}>
                    <AntDesign name={modalIcon} size={35} color="white" style={{paddingRight:10}}/>
                    <SivariaText fontSize={35}>{title}</SivariaText>
                </View>
                {/*<Br />*/}                
                <ScrollView style={{flex:3, width:'100%', padding:10}}>
                    <SivariaText fontSize={20} color={'black'} >{message}</SivariaText>
                </ScrollView>
                {/*<Br />*/}
                <View style={{flex:0.4, width:'100%', alignItems:'center', justifyContent: 'center', borderTopWidth:2, borderTopColor: 'grey'}}>
                    <SivariaButton onPress={() => setIsVisible(false)}>
                        <SivariaText isBold={true}>
                            CERRAR
                        </SivariaText>
                    </SivariaButton>
                </View>            
            </View>

        </Modal>
    );
}

function Br() {
    return <View style={styles.gap} />;
}

const styles = StyleSheet.create({
    modalContainer: {
      alignItems: 'center',
      justifyContent: 'center',
      flex: 1,
    },
    gap: {
      height: 10
    },
    titleText: {
        fontSize: 30,
        fontWeight: 'bold',
    }
  });

export default ModalComponent;