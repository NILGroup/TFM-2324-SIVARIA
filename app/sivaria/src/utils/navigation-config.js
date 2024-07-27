import { Text } from "react-native"

export const theme = {

}

export const config = {
    /*screens: {
        Root: {
            path: "/",
            initialRouteName: "/",
            screens: {
                LoginScreen:"/",
                RegisterScreen: "/register",
                HomeScreen: "/home"
            }
        }
    }*/
    initialRouteName: "/",
    screens: {
        // siv://login -> LoginScreen
        Login: "login",
        // siv://details/1 -> DetailsScreen with param id: 1
        // siv://register -> RegisterScreen
        Register: "register",
        ForgotPassword: "forgot-password",
        /*RecoveryPassword: "recovery-password",*/
        RecoveryPassword: {
            path: "recovery-password/:token/:email",
            parse: {
                token: (token) => `${token}`,
                email: (email) => `${email}`
            },
        },
        /*
        RecoverPassword: {
            path: "recovery-password?email=:email",
        },
        */
        /*
        Profile: {
            path: 'user/:id/:section',
            parse: {
              id: (id) => `user-${id}`,
            },
            stringify: {
              id: (id) => id.replace(/^user-/, ''),
            },
          },
          */
        Dashboard: {
            initialRouteName: 'dashboard',
            screens: {
                Home: "dashboard/home",
                History: "dashboard/history",
                Profile: "dashboard/profile",
            }
        },
        EditData: "edit-data",
        YoungstersQuestionnaireSivaria: "young-questionnaire",
        ParentsQuestionnaireSivaria: "family-questionnaire",
        ProfessionalsQuestionnaireSivaria: "professional-questionnaire",
        
    },
}

export const linking = 
{
    //prefixes: ["siv://127.0.0.1:8080/--/"], // It is not supported in Web, so it will be ignored.
    prefixes: ["siv://"],
    config
}

export const fallback = <Text>Cargando...</Text>