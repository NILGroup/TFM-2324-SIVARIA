import { Pressable } from "react-native";

const SivariaButton = ({onPress, children }) => {
    return (
        <Pressable 
            style={
                ({pressed}) => [
                    {
                        backgroundColor: pressed ? '#7bdcb5' : '#006E51',
                        borderColor: pressed ? '#7bdcb5' : '#024332',
                    },
                    {
                        //padding: 10,
                        alignItems: 'center',
                        justifyContent: 'center',
                        borderRadius: 8,
                        borderWidth: 1,
                        borderColor: '#024332',
                        //marginTop: 10,
                        width: '80%',
                        height: '50%'
                    },
                    //{justifyContent: 'flex-end'}
                ]
            }
            onPress={onPress}
        >
            { children }
        </Pressable>
    );
}

export default SivariaButton;