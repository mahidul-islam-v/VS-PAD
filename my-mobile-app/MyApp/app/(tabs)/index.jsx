import { View, Text, StyleSheet, ImageBackground } from "react-native";
import icedCoffeeImg from "@/assets/images/Iced-Coffee.jpg";
import React from "react";

const app = () => {
    return (
        <View style={styles.container}>
            <ImageBackground
                source={icedCoffeeImg}
                resizeMode="cover"
                style={styles.img}
            >
                <Text style={styles.text}>Coffee Shop</Text>
            </ImageBackground>
        </View>
    );
};

export default app;

const styles = StyleSheet.create({
    container: {
        flex: 1,
        flexDirection: "column",
    },
    text: {
        color: "white",
        fontSize: 42,
        fontWeight: "bold",
        textAlign: "center",
    },
    img: {
        width: "100%",
        height: "100%",
        flex: 1,
        justifyContent: "center",
        resizeMode: "cover",
    },
});
