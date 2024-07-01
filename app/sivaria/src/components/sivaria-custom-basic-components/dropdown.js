import React from 'react'
import { StyleSheet } from 'react-native';
import RNPickerSelect from "react-native-picker-select";
import { Platform } from 'react-native';

const Dropdown = ({items, placeholder, value, onValueChange}) => {
  const stylesSelected = '';

  return(
      <RNPickerSelect
          items={items}
          placeholder={placeholder}
          value={value}
          onValueChange={onValueChange}
          style={pickerSelectStyles.inputAndroid}
      />
  );

}

const pickerSelectStyles = StyleSheet.create({
    inputIOS: {
      fontSize: 16,
      paddingVertical: 12,
      paddingHorizontal: 10,
      borderWidth: 1,
      borderColor: 'gray',
      borderRadius: 4,
      color: 'black',
      paddingRight: 30,
    },
    inputAndroid: {
      fontSize: 16,
      paddingHorizontal: 10,
      paddingVertical: 8,
      borderWidth: 0.5,
      borderColor: 'red',
      borderRadius: 8,
      color: 'blue',
      paddingRight: 30,
    },
});

export default Dropdown;