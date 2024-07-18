import React, { useEffect, useRef, useState } from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { UserStackNavigator } from './src/navigation/stack';
import { linking, fallback } from './src/utils/navigation-config';
import { Platform, Linking } from 'react-native';
import { getItemLocalStorage, setItemLocalStorage } from './src/utils/general-local-storage';
import LoadingScreen from './src/screens/loading-screen';

import { AuthContext } from './src/context/auth-context';
//import AuthProvider from './src/context/auth-provider';
import { ToastProvider } from 'react-native-toast-notifications';
import { UserContext } from './src/context/user-context';

import useUserData from './src/utils/user-user-data-hook';

//import { Bounce, ToastContainer } from 'react-toastify';
//import 'react-toastify/dist/ReactToastify.css';

export default function App() {
  //const { isAuthenticated, setIsAuthenticated } = useContext(AuthContext);
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  
  const [userId, setUserId] = useState(0);
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [rol, setRol] = useState('');
  const [rolSlug, setRolSlug] = useState('');
  const [emailParent1, setEmailParent1] = useState('');
  const [emailParent2, setEmailParent2] = useState('');

  const [loading, setLoading] = useState(true);

  const navigationRef = useRef(null);
  const routeNameRef = useRef(null);

  const [initialState, setInitialState] = useState();

  const { updateUserStateVariables } = useUserData();

  const checkToken = async() => {
    const token = await getItemLocalStorage('userToken');
    //const savedRoute = await getItemLocalStorage('currentRoute');
    //removeItemLocalStorage('userToken');
    //console.log('Token');
    //console.log(token);
    //console.log(savedRoute);
    if(token) {
      setIsAuthenticated(true);
    }
    //setLoading(false);
    /*
    if (navigationRef.current && savedRoute) {
      setTimeout(() => {
        navigationRef.current.navigate(savedRoute);
      }, 0);
    }
      */
  }

  const checkUserData = async() => {
    //updateUserStateVariables();
    //console.log('ESTOY EN CHECKUSER DATA DEL APP.JS');
    
    let userIdLocal = await getItemLocalStorage('userId');
    let emailLocal = await getItemLocalStorage('email');
    let firstNameLocal = await getItemLocalStorage('firstName');
    let lastNameLocal = await getItemLocalStorage('lastName');
    let phoneNumberLocal = await getItemLocalStorage('phoneNumber');
    let rolLocal = await getItemLocalStorage('rol');
    let rolSlugLocal = await getItemLocalStorage('rolSlug');
    let emailParent1Local = await getItemLocalStorage('emailParent1');
    let emailParent2Local = await getItemLocalStorage('emailParent2');
    
    if(userIdLocal) {
      setUserId(userIdLocal);
    }
    if(emailLocal) {
      setEmail(emailLocal);
    }
    if(firstNameLocal) {
      setFirstName(firstNameLocal);
    }
    if(lastNameLocal) {
      setLastName(lastNameLocal);
    }
    if(phoneNumberLocal) {
      setPhoneNumber(phoneNumberLocal);
    }
    if(rolLocal) {
      setRol(rolLocal);
    }
    if(rolSlugLocal) {
      setRolSlug(rolSlugLocal);
    }
    if(emailParent1Local) {
      setEmailParent1(emailParent1Local);
    }
    if(emailParent2Local) {
      setEmailParent2(emailParent2Local);
    }

  }

  const getCurrentRoute = async () => {
    let savedRoute = await getItemLocalStorage('currentRoute') ?? undefined;
    if(savedRoute !== undefined) {
      //console.log('SAVED ROUTE = ' + savedRoute);
      setInitialState(savedRoute);
    }
    //console.log('INITIAL STATE = ' + initialState);
    //console.log('Saved Route');
    //removeItemLocalStorage('currentRoute');
    /*
    console.log('SAVED ROUTE = ' + savedRoute);
    //console.log((navigationRef.current) ? navigationRef.current.getCurrentRoute().name : 'NULL');
    console.log(navigationRef.current);
    if (savedRoute && navigationRef.current) {
      console.log('DENTRO DEL IF. SAVED ROUTE Y NAVIGATIONREF.CURRENT NO SON NULOS');
      navigationRef.current.navigate(savedRoute);
    }
      */
  };

  const restoreRoute = async () => {
    try {
      const initialUrl = await Linking.getInitialURL();

      if (initialUrl === null) {
        // Only restore state if there's no deep link and we're not on web
        const savedStateString = await getItemLocalStorage('currentRoute');
        const state = savedStateString
          ? JSON.parse(savedStateString)
          : undefined;
          
        if (state !== undefined) {
          setInitialState(state);
        }
      }
    } finally {
      //setIsReady(true);
    }
  };

  // Each time a page is loaded, it is checked if the user is authenticatd or not, and it is checked the user info.
  useEffect(() => {
    if(loading) {
      checkToken();
      checkUserData();
      // Get the saved route on app load
      //getCurrentRoute();
      restoreRoute();
      setLoading(false);
    }
  }, []);

  // Used to save the current route before the component is dismounted
  /*
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
  */
  /*
  // Get the saved route on app load
  useEffect(() => {
    getCurrentRoute();
  }, []);
  */

  if (loading) {
    return (
        <LoadingScreen />
    );
  }

  return (
      <ToastProvider normalColor='skyblue' 
        placement={Platform.OS === 'web' ? 'top' : 'bottom'}
        duration={2000}
      >
        <AuthContext.Provider value={{ isAuthenticated, setIsAuthenticated }}>
          <UserContext.Provider value={{ 
            userId, setUserId,
            firstName, setFirstName,
            lastName, setLastName,
            password, setPassword,
            email, setEmail,
            phoneNumber, setPhoneNumber,
            rol, setRol,
            rolSlug, setRolSlug,
            emailParent1, setEmailParent1,
            emailParent2, setEmailParent2 }}
          >
            <NavigationContainer
              ref={navigationRef}
              linking={linking}
              fallback={fallback}
              initialState={initialState}
              onStateChange={(state) => {
                //console.log('CAMBIO DE ESTADO');
                //const previousRouteName = routeNameRef.current;
                //const currentRouteName = navigationRef.current.getCurrentRoute().name;
                //if (previousRouteName !== currentRouteName) {
                  //console.log('NUEVO ESTADO = ' + currentRouteName);
                //}
                //routeNameRef.current = currentRouteName;
                //setItemLocalStorage('currentRoute', currentRouteName);
                setItemLocalStorage('currentRoute', JSON.stringify(state));
                //AsyncStorage.setItem(PERSISTENCE_KEY, JSON.stringify(state))
              }}
            >
                <UserStackNavigator/>
            </NavigationContainer>
          </UserContext.Provider>
        </AuthContext.Provider>
      </ToastProvider>
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