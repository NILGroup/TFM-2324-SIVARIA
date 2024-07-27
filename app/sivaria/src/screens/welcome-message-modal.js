import { View, Pressable, Text, Modal } from "react-native";
import { AntDesign } from "@expo/vector-icons";
import SivariaText from "../components/sivaria-text";
import WelcomeMessage from "./welcome-message";

export const WelcomeMessageModal = ({isVisible, setModalVisible}) => {
    return (
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
                <WelcomeMessage/>
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
    );
}