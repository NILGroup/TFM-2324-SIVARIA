import React, { useState } from 'react';
import { View, Text, StyleSheet, Pressable } from 'react-native';

export default function SivariaRadioButton({ data, option, onSelect }) {

    const [userOption, setUserOption] = useState(option);

    const selectHandler = (value) => {
        onSelect(value);
        setUserOption(value);
    };

    return (
        <View style={{flexDirection:'row', justifyContent:'space-between'}}>
            {data.map((item) => {
                return (
                    <Pressable 
                    key={item.value+'_button'}    
                    style={[
                            item.value === userOption ? styles.selected : styles.unselected,
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
                        onPress={() => selectHandler(item.value)}
                    >
                        <Text 
                            key={item.value+'_text'} 
                            style={item.value === userOption ? styles.selectedOption : styles.unselectedOption}
                        >
                            {item.label}
                        </Text>
                    </Pressable>
                );
            })}
        </View>
    );
}

const styles = StyleSheet.create({
    selectedOption: {
        fontSize: 20,
        color: 'white',
        textAlign: 'center',
    },
    unselectedOption: {
        fontSize: 20,
        color: 'black',
        textAlign: 'center',
    },
    unselected: {
      backgroundColor: '#f1f1f1',
    },
    selected: {
      backgroundColor: '#006E51',
    },
});