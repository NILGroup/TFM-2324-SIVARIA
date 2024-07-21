import { View, Text, ActivityIndicator, StyleSheet } from "react-native";
import SivariaInput from "../../../components/sivaria-input";

const ParentsQuestionnaireSivariaScreen = () => {
    return(
        <View style={{flex:1, backgroundColor: 'white'}}>
            
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      alignItems: 'center',
      justifyContent: 'center',
      margin: 20,
    },
   containerButtonStyle:{
            display: 'flex',
            flexDirection: 'row',
            justifyContent: 'flex-end',
            paddingLeft: 10,
            paddingRight: 30,
          }
  });

export default ParentsQuestionnaireSivariaScreen;