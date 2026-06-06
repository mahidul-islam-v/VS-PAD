import { View, Text, StyleSheet, ImageBackground } from "react-native";
import icedCoffeeImg from "@/assets/images/Iced Coffee.jpeg";
import React from "react";

const app = () => {
    return (
        <View style={styles.container}>
            <ImageBackground
                src={icedCoffeeImg}
                resizeMode="cover"
                stle={styles.img}
            ></ImageBackground>
            <Text style={styles.text}>Cofee Shop</Text>
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
