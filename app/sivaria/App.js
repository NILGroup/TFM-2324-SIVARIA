import React, { useEffect, useRef, useState } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { UserStackNavigator /*, LoggedUserStack, NonLoggedUserStack */} from './src/navigation/stack';
import { linking, fallback } from './src/utils/navigation-config';
import { View, ActivityIndicator, AppState, Platform } from 'react-native';
import { getItemLocalStorage, setItemLocalStorage } from './src/utils/general-local-storage';
import stylesSivaria from './src/styles/styles-sivaria';
import LoadingScreen from './src/screens/loading-screen';

export default function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [loading, setLoading] = useState(true);
  const navigationRef = useRef(null);
  const routeNameRef = useRef(null);

  const checkTokenAndRoute = async() => {
    const token = await getItemLocalStorage('userToken');
    const savedRoute = await getItemLocalStorage('currentRoute');
    
    console.log('Token');
    console.log(token);
    console.log(savedRoute);
    if(token) {
      setIsAuthenticated(true);
    }
    setLoading(false);
    /*
    if (navigationRef.current && savedRoute) {
      setTimeout(() => {
        navigationRef.current.navigate(savedRoute);
      }, 0);
    }
      */
  }

  // Each time a page is loaded, it is checked if the user is authenticatd or not.
  useEffect(() => {
    checkTokenAndRoute();
  }, []);

  // Used to save the current route before the component is dismounted
  useEffect(() => {
    const saveCurrentRoute = () => {
      const currentRoute = (navigationRef !== null) ? navigationRef.current.getCurrentRoute().name : null;
      console.log('Current Route');
      console.log(currentRoute);
      if (currentRoute) {
        setItemLocalStorage('currentRoute', currentRoute);
      }
    };

    if (Platform.OS !== 'web') {
      const handleAppStateChange = (nextAppState) => {
        if (nextAppState === 'background') {
          saveCurrentRoute();
        }
      };

      const subscription = AppState.addEventListener('change', handleAppStateChange);

      return () => {
        subscription.remove();
      };

    } else {
      window.addEventListener('beforeunload', saveCurrentRoute);

      return () => {
        window.removeEventListener('beforeunload', saveCurrentRoute);
      };
    }
  }, []);

  // Get the saved route on app load
  useEffect(() => {
    const getCurrentRoute = async () => {
      const savedRoute = await getItemLocalStorage('currentRoute');
      console.log('Saved Route');
      console.log(savedRoute);
      if (savedRoute && navigationRef.current) {
        navigationRef.current.navigate(savedRoute);
      }
    };

    getCurrentRoute();
  }, []);

  if (loading) {
    return (
        <LoadingScreen />
    );
  }

  return (
    <NavigationContainer
      ref={navigationRef}
      linking={linking}
      fallback={fallback}
      onReady={() => {
        routeNameRef.current = navigationRef.current.getCurrentRoute().name;
      }}
      onStateChange={() => {
        const previousRouteName = routeNameRef.current;
        const currentRouteName = navigationRef.current.getCurrentRoute().name;
        if (previousRouteName !== currentRouteName) {
          setItemLocalStorage('currentRoute', currentRouteName);
        }
        routeNameRef.current = currentRouteName;
      }}
    >

      <UserStackNavigator isAuthenticated={isAuthenticated} setIsAuthenticated={setIsAuthenticated}/>
      
    </NavigationContainer>
  );
}
//<UserStackNavigator isAuthenticated={isAuthenticated}/>
/*
export default function App() {
  return (
    <View style={styles.container}>
      <Text>Open up App.js to star working on your app!</Text>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
*/