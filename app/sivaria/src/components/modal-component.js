import { Modal, Pressable, Text, View, StyleSheet } from "react-native";

const ModalComponent = ({animationType, setIsVisible, isVisible, title, message}) => {
    
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
            <View style={styles.container}>
                <Text styles={styles.titleText}>{title}</Text>
                <Br />
                <Text>{message}</Text>
                <Br />
                <Pressable onPress={() => setIsVisible(false)}>
                    <Text>Cerrar</Text>
                </Pressable>            
            </View>

        </Modal>
    );
}

function Br() {
    return <View style={styles.gap} />;
}

const styles = StyleSheet.create({
    container: {
      alignItems: 'center',
      flex: 1,
      justifyContent: 'center'
    },
    gap: {
      height: 10
    },
    titleText: {
        fontSize: 20,
    }
  });

export default ModalComponent;