import { useState } from 'react';
import { ScrollView, View, Text, Pressable, Linking, Platform } from 'react-native';

import LoadingScreen from '../loading-screen';
import { useToast } from 'react-native-toast-notifications';

const ContactScreen = ({navigation}) => {
    const [isLoading, setIsLoading] = useState(false);

    const toast = useToast();

    function callPhoneNumber(phoneNumber) {
        let phoneNumberURL = phoneNumber;
        if(Platform.OS !== 'android') {
            phoneNumberURL = `tel:${phoneNumber}`;
        }
        else {
            phoneNumberURL = `tel:${phoneNumber}`;
        }
        Linking.canOpenURL(phoneNumberURL)
        .then(supported => {
            if (!supported) {
                toast.show(
                    'Número de teléfono no disponible',
                    {
                        type: 'danger'
                    }
                );
            } else {
                return Linking.openURL(phoneNumberURL);
            }
        })
        .catch(err => console.log(err));
    }

    if(isLoading) {
        return (
            <LoadingScreen />
        );
    }

    return (
      <ScrollView>
        <View style={{height: 700, backgroundColor: 'white', padding: 20, justifyContent: 'space-between'}}>
            <View style={{padding:5}}>
                <Text style={{fontWeight: 'bold', fontSize:20}}>
                    ¡No estás sólo!
                </Text>
                <Text> 
                    Estamos aquí para ayudarte. Puedes contactar a las siguientes organizaciones para pedir ayuda, y estarán siempre dispuestos a
                    escucharte darte las mejores indicaciones.
                </Text>
            </View>
            <View style={{backgroundColor: '#DCDCDC', padding:10, justifyContent:'space-between', borderWidth: 1, borderRadius: 8}}>
                <View style={{padding: 5}}>
                    <Text style={{fontWeight: 'bold', fontSize:20}}>
                        024
                    </Text>
                </View>
                <View style={{padding:5}}>
                    <Text>
                        <Text style={{fontWeight:'bold'}}>Ministerio de Sanidad</Text>. Disponible las 24 horas, todos los días de la semana.
                    </Text>
                </View>
                <View style={{height: 50, padding:5, justifyContent: 'center'}}>
                    <Pressable 
                        style={
                            ({pressed}) => [
                                {
                                    backgroundColor: pressed ? '#7bdcb5' : '#006E51',
                                    borderColor: pressed ? '#7bdcb5' : '#024332',
                                },
                                {
                                    height: 30,
                                    alignItems: 'center', 
                                    justifyContent: 'center',
                                    borderWidth: 1,
                                    borderRadius: 8
                                },
                            ]
                        } 
                        onPress={() => callPhoneNumber('024')}
                    >
                        <Text style={{color: 'white', fontWeight: 'bold'}}>
                            LLAMAR
                        </Text>
                    </Pressable>
                </View>
            </View>
            
            <View style={{backgroundColor: 'lightgrey', padding:10, justifyContent:'space-between', borderWidth: 1, borderRadius: 8}}>
                <View style={{padding: 5}}>
                    <Text style={{fontWeight: 'bold', fontSize:20}}>
                        112 o 091
                    </Text>
                </View>
                <View style={{padding:5}}>
                    <Text>
                        <Text style={{fontWeight:'bold'}}>Servicios de emergencia</Text>. Llamar en caso de riesgo inminente. Disponible las 24 horas, todos los días de la semana
                    </Text>
                </View>
                <View style={{height: 50, padding:5, justifyContent: 'center'}}>
                    <Pressable 
                        style={
                            ({pressed}) => [
                                {
                                    backgroundColor: pressed ? '#7bdcb5' : '#006E51',
                                    borderColor: pressed ? '#7bdcb5' : '#024332',
                                },
                                {
                                    height: 30,
                                    alignItems: 'center', 
                                    justifyContent: 'center',
                                    borderWidth: 1,
                                    borderRadius: 8
                                },
                            ]
                        } 
                        onPress={() => callPhoneNumber('112')}
                    >
                        <Text style={{color: 'white', fontWeight: 'bold'}}>
                            LLAMAR 112
                        </Text>
                    </Pressable>
                </View>
                <View style={{height: 50, padding:5, justifyContent: 'center'}}>
                    <Pressable 
                        style={
                            ({pressed}) => [
                                {
                                    backgroundColor: pressed ? '#7bdcb5' : '#006E51',
                                    borderColor: pressed ? '#7bdcb5' : '#024332',
                                },
                                {
                                    height: 30,
                                    alignItems: 'center', 
                                    justifyContent: 'center',
                                    borderWidth: 1,
                                    borderRadius: 8
                                },
                            ]
                        } 
                        onPress={() => callPhoneNumber('091')}
                    >
                        <Text style={{color: 'white', fontWeight: 'bold'}}>
                            LLAMAR 091
                        </Text>
                    </Pressable>
                </View>
            </View>
            
            <View style={{backgroundColor: 'lightgrey', padding:10, justifyContent:'space-between', borderWidth: 1, borderRadius: 8}}>
                <View style={{padding: 5}}>
                    <Text style={{fontWeight: 'bold', fontSize:20}}>
                        717 003 717
                    </Text>
                </View>
                <View style={{padding:5}}>
                    <Text>
                        <Text style={{fontWeight:'bold'}}>Teléfono de la esperanza</Text>. Es una ONG que ofrece servicio gratuito para apoyar a las personas que se encuentran en situación de crisis. Disponible las 24 horas, todos los días de la semana
                    </Text>
                </View>
                <View style={{height: 50, padding:5, justifyContent: 'center'}}>
                    <Pressable 
                        style={
                            ({pressed}) => [
                                {
                                    backgroundColor: pressed ? '#7bdcb5' : '#006E51',
                                    borderColor: pressed ? '#7bdcb5' : '#024332',
                                },
                                {
                                    height: 30,
                                    alignItems: 'center', 
                                    justifyContent: 'center',
                                    borderWidth: 1,
                                    borderRadius: 8
                                },
                            ]
                        } 
                        onPress={() => callPhoneNumber('717003717')}
                    >
                        <Text style={{color: 'white', fontWeight: 'bold'}}>
                            LLAMAR
                        </Text>
                    </Pressable>
                </View>
            </View>
            {/*
            <Text>911385385</Text>        
            <Text>
                Teléfono contra el suicidio. Es un teléfono está a cargo de profesionales de la salud mental. Disponible las 24 horas, todos los días de la semana
            </Text>
            <Button />
            
            <Text>900 20 20 10</Text>        
            <Text>
                Fundación ANAR. Es una organización sin ánimo de lucro que ayuda a niños/as y adolescentes en riesgo. Disponible las 24 horas, todos los días de la semana.
            </Text>
            <Button />
            
            <Text>900 107 917</Text>        
            <Text>
                Cruz Roja. No es una línea dedicada al suicidio, pero también puede atender este tipo de llamadas. Disponible de lunes a viernes laborables, de 10:00 a 14:00 y de 16:00 a 20:00.</Text>
            <Button />
            */}
        </View>
      </ScrollView>
  );
}
  
export default ContactScreen;