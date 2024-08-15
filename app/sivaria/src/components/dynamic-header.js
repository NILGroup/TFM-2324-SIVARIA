import * as React from 'react';
import { Text, View, StyleSheet, Animated } from 'react-native';

const Max_Header_Height = 100;
const Min_Header_Height = 50;
const Scroll_Distance = Max_Header_Height - Min_Header_Height;

const DynamicHeader = ({animHeaderValue, children}) => {
    const animateHeaderHeight =  animHeaderValue.interpolate({
        inputRange: [0, Scroll_Distance],
        outputRange: [Max_Header_Height , Min_Header_Height],
        extrapolate: 'clamp'
    });
    return (
        <Animated.View
            style={[
                {
                    flexDirection: 'center', 
                    alignItems: 'center', 
                    justifyContent: 'center', 
                    backgroundColor: '#006E51'
                },
                {
                    height: animateHeaderHeight
                }
            ]}
        >
            {children}
        </Animated.View>
    );
};

export default DynamicHeader;