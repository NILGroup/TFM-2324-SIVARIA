import { Text } from "react-native"

export const theme = {

}

export const config = {
    screens: {
        Root: {
            path: "/",
            initialRouteName: "/",
            screens: {
                LoginScreen:"/",
                RegisterScreen: "/register",
                HomeScreen: "/home"
            }
        }
    }
}

export const linking = 
{
    prefixes: ["siv://127.0.0.1:8080/--/"], // It is not supported in Web, so it will be ignored.
    config
}

export const fallback = <Text>Cargando...</Text>