import { Pressable } from "react-native";
import SivariaText from "./sivaria-text";

const SivariaButton = ({onPress, message, disabled=false}) => {
    return (
        <Pressable 
            style={ (disabled) ?
                {
                    //padding: 10,
                    alignItems: 'center',
                    justifyContent: 'center',
                    borderRadius: 8,
                    borderWidth: 1,
                    //marginTop: 10,
                    width: '80%',
                    height: '50%',
                    backgroundColor: '#024332',
                    borderColor: '#024332',
                }
                :
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
                        //marginTop: 10,
                        width: '80%',
                        height: '50%'
                    },
                    //{justifyContent: 'flex-end'}
                ]
            }
            onPress={onPress}
            disabled={disabled ? true : false}
        >
            <SivariaText isBold={true} color={disabled ? 'grey' : 'white'}>
                { message }
            </SivariaText>
        </Pressable>
    );
}

export default SivariaButton;