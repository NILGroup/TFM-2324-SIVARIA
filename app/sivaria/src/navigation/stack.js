import { createNativeStackNavigator } from "@react-navigation/native-stack";
import LoginScreen from "../screens/non-logged-users/login-screen";
import HomeScreen from "../screens/logged-users/home-screen";
import RegisterScreen from "../screens/non-logged-users/register-screen";
import { Platform } from "react-native";
import { DashboardTabsScreen } from "./logged-tab-stack";
import { useContext } from "react";
import { AuthContext } from "../context/auth-context";
import EditDataScreen from "../screens/logged-users/edit-data-screen";
import { UserContext } from "../context/user-context";
//import YoungstersQuestionnaireSivariaScreen from "../screens/logged-users/questionnaire-sivaria/youngsters-questionnaire-screen.js";
//import ParentsQuestionnaireSivariaScreen from "../screens/logged-users/questionnaire-sivaria/parents-questionnaire-screen";
//import ProfessionalsQuestionnaireSivariaScreen from "../screens/logged-users/questionnaire-sivaria/professionals-questionnaire-screen";
import ForgotPasswordScreen from "../screens/non-logged-users/forgot-password-screen";
import RecoveryPasswordScreen from "../screens/non-logged-users/recovery-password-screen";
import { YoungstersStackNavigator } from "./questionnaires-navigators/youngsters-questionnaire-navigator";
import { FamiliesStackNavigator } from "./questionnaires-navigators/families-questionnaire-navigator";
import { ProfessionalsStackNavigator } from "./questionnaires-navigators/professionals-questionnaire-navigator";

const UserStack = createNativeStackNavigator();

export const UserStackNavigator = ({navigation}) => {
  const user = useContext(AuthContext);
  const userData = useContext(UserContext);

  return (
    <UserStack.Navigator screenOptions={ { headerShown: Platform.OS !== 'web' ? true : false } }>
      {
        /*console.log(user.isAuthenticatedRef.current)*/
      }
      {user.isAuthenticated ? ( 
        <>
          <UserStack.Screen name="Dashboard" component={DashboardTabsScreen}/>     
          <UserStack.Screen name="EditData" component={EditDataScreen}/>
          <UserStack.Screen name="YoungstersQuestionnaireSivaria" component={YoungstersStackNavigator}/>
          <UserStack.Screen name="ParentsQuestionnaireSivaria" component={FamiliesStackNavigator}/>
          <UserStack.Screen name="ProfessionalsQuestionnaireSivaria" component={ProfessionalsStackNavigator}/>
        </>
      ) : (
        <>
          <UserStack.Screen name="Login" component={LoginScreen}/>
          <UserStack.Screen name="Register" component={RegisterScreen} />          
          <UserStack.Screen name="ForgotPassword" component={ForgotPasswordScreen} />
          <UserStack.Screen name="RecoveryPassword" component={RecoveryPasswordScreen} />
        </>    
      )}
    </UserStack.Navigator>
  );
}

/*
export const NonLoggedUserStack = () => {
  return (
    <Stack.Navigator screenOptions={{headerShown: false}}>
      <Stack.Screen name="Login" component={LoginScreen} />
      <Stack.Screen name="Register" component={RegisterScreen} />
    </Stack.Navigator>
  );
}


export const LoggedUserStack = () => {
  return (
    <Stack.Navigator screenOptions={{headerShown: false}}>
      <Stack.Screen name="Home" component={HomeScreen} />
    </Stack.Navigator>
  );
};
*/