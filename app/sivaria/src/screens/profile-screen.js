import React, { useEffect, useState } from 'react';
import { StyleSheet, ActivityIndicator, ScrollView, SafeAreaView, View, Text, TextInput, Pressable, Alert } from 'react-native';
import Dropdown from '../components/dropdown';
import ShowHidePasswordInput from '../components/show-hide-password-input';
import axiosInstance from '../utils/axios-config-web';
import stylesSivaria from '../styles/styles-sivaria';
import PhoneInput from "react-native-phone-input";
import LoadingScreen from './loading-screen';

const ProfileScreen = ({navigation}) => {

    

    return (
        <SafeAreaView style={stylesSivaria.tabContainer}>
            <View>
                <Text>PROFILE SCREEN</Text>
            </View>
        </SafeAreaView>
    );
}

export default ProfileScreen;