import { useState, useEffect, useRef } from "react";
import * as Device from 'expo-device';
import * as Notifications from 'expo-notifications';
import Constants from 'expo-constants';
import { Platform } from "react-native";
/*
const initialState = {
    notification: Notifications.Notification,
    expoPushToken: Notifications.ExpoPushToken,
};

// Define the function to get the push notification state
export const getPushNotificationState = () => {
    return { ...initialState };
};
*/
export interface PushNotificationState {
    notification?: Notifications.Notification,
    expoPushToken?: Notifications.ExpoPushToken,
}

export const usePushNotifications = (): PushNotificationState => {
    Notifications.setNotificationHandler({
        handleNotification: async () => ({
            shouldPlaySound: true,
            shouldShowAlert: true,
            shouldSetBadge: false,
        })
    });

    const [expoPushToken, setExpoPushToken] = useState<Notifications.ExpoPushToken | undefined>();
    const [notification, setNotification] = useState<Notifications.Notification | undefined>();

    const notificationListener = useRef<Notifications.Subscription>();
    const responseListener = useRef<Notifications.Subscription>();

    async function registerForPushNotificationsAsync() {
        let token;
        
        // It checks if the device is a simulator or not. The push notifications do not work on simulators
        if(Device.isDevice) {
            const { status: existingStatus } = await Notifications.getPermissionsAsync();

            let finalStatus = existingStatus;

            if(existingStatus !== 'granted') {
                // Permissions for notifications is not granted, so they must be requested 
                const { status } = await Notifications.requestPermissionsAsync();
                finalStatus = status;
            }
            
            // If the final status is still no granted, then an error is shown
            if(finalStatus !== 'granted') {
                //alert('Fallo a la hora de conseguir el push token');
            }
            if(Platform.OS !== 'web') {
                token = await Notifications.getExpoPushTokenAsync({
                    projectId: Constants.expoConfig?.extra?.eas?.projectId,
                });
            }

            if(Platform.OS === 'android') {
                Notifications.setNotificationChannelAsync('default', {
                    name: 'default',
                    importance: Notifications.AndroidImportance.MAX,
                    vibrationPattern: [0, 250, 250, 250],
                    lightColor: '#ff231f7c'
                })
            }

            return token;

        }
        else {
            console.warn('The app is executing in a simulator. Push notifications will not work.');
        }
    }

    useEffect(() => {
        registerForPushNotificationsAsync().then((token) => {
            setExpoPushToken(token);
        });

        notificationListener.current = Notifications.addNotificationReceivedListener((notification) => {
            setNotification(notification);
        });

        responseListener.current = Notifications.addNotificationResponseReceivedListener((response) => {
            console.log(response);
        });

        return () => {
            Notifications.removeNotificationSubscription(
                notificationListener.current
            );

            Notifications.removeNotificationSubscription(
                responseListener.current
            );
        };
    }, []);

    return {
        expoPushToken,
        notification,
    };
};


