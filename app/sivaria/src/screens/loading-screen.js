import { View, ActivityIndicator } from "react-native";
import stylesSivaria from "../styles/styles-sivaria";

const LoadingScreen = () => {
    return(
        <View style={stylesSivaria.loading}>
            <ActivityIndicator size="large" color="#006E51" />
        </View>
    );
}

export default LoadingScreen;