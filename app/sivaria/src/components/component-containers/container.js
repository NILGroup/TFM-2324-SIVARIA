import React from "react";
import { StyleSheet, SafeAreaView, StatusBar, View, ScrollView, Dimensions, Platform, NativeModules } from "react-native";

const { StatusBarManager } = NativeModules;

const { height } = Dimensions.get('window');

export default class Container extends React.Component {
  state = {
    screenHeight: height,
  };

  onContentSizeChange = (contentWidth, contentHeight) => {
    this.setState({ screenHeight: contentHeight });
  };

  render() {
    const scrollEnabled = this.state.screenHeight > height;
    //console.log(scrollEnabled);
    //console.log(this.state.screenHeight);
    //console.log(height);
    return (
      <SafeAreaView style={styles.container}>
        <ScrollView
          style={{ flex: 1 }}
          contentContainerStyle={styles.scrollview}
          scrollEnabled={scrollEnabled}
          onContentSizeChange={this.onContentSizeChange}
        >
          <View style={styles.content}>
            {this.props.children}
          </View>
        </ScrollView>
      </SafeAreaView>
    );
  }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#006E51',
        //paddingVertical: Platform.OS === 'android' ? StatusBarManager.HEIGHT : 0,
    },
    scrollview: {
        flexGrow: 1,
    },
    content: {
        flexGrow: 1,
        //justifyContent: "space-between",
        //padding: 10,
    },
});