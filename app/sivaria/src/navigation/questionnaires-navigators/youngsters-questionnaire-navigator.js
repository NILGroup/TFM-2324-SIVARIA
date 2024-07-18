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
import YoungstersQuestionnaireSivariaScreen from "../screens/logged-users/questionnaire-sivaria/youngsters-questionnaire-screen.js";
import ParentsQuestionnaireSivariaScreen from "../screens/logged-users/questionnaire-sivaria/parents-questionnaire-screen";
import ProfessionalsQuestionnaireSivariaScreen from "../screens/logged-users/questionnaire-sivaria/professionals-questionnaire-screen";
import ForgotPasswordScreen from "../screens/non-logged-users/forgot-password-screen";
import RecoveryPasswordScreen from "../screens/non-logged-users/recovery-password-screen";

const YoungstersStack = createNativeStackNavigator();

export const YoungstersStackNavigator = ({navigation}) => {

    return (
        <YoungstersStack.Navigator screenOptions={{headerShown: false}}>
            <YoungstersStack.Screen name="Login" component={LoginScreen} />
        </YoungstersStack.Navigator>
    );
}