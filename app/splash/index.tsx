import AsyncStorage from "@react-native-async-storage/async-storage";
import MaskedView from '@react-native-masked-view/masked-view';
import * as Google from "expo-auth-session/providers/google";
import { LinearGradient } from 'expo-linear-gradient';
import { useRouter } from 'expo-router';
import * as WebBrowser from "expo-web-browser";
import * as React from "react";
import { useEffect } from "react";
import { Image, StatusBar, StyleSheet, Text, TouchableOpacity, View } from "react-native";
import { SafeAreaView } from 'react-native-safe-area-context';

WebBrowser.maybeCompleteAuthSession();

export default function SplashScreen() {
  const router = useRouter();
  const [request, response, promptAsync] = Google.useAuthRequest({
    webClientId: process.env.EXPO_PUBLIC_GOOGLE_WEB_ID,
    androidClientId: process.env.EXPO_PUBLIC_GOOGLE_ANDROID_ID,
    iosClientId: process.env.EXPO_PUBLIC_GOOGLE_IOS_ID,
  });

  const [userInfo, setUserInfo] = React.useState(null);

  const handleSignInWithGoogle = async () => {
    const user = await AsyncStorage.getItem("@user");
    if (!user) {
      if (response?.type === "success") {
        await getUserInfo(response.authentication?.accessToken as string);
      }
    } else {
      setUserInfo(JSON.parse(user));
    }
  };

  const getUserInfo = async (token: string) => {
    if (!token) return;
    try {
      const response = await fetch(
        "https://www.googleapis.com/oauth2/v3/userinfo",
        {
          headers: { Authorization: `Bearer ${token}` },
        }
      );
      const userInfoResponse = await response.json();
      await AsyncStorage.setItem("@user", JSON.stringify(userInfoResponse));
      setUserInfo(userInfoResponse);
    } catch (e) {
      console.log(e);
    }
  };

  useEffect(() => {
    handleSignInWithGoogle();
  }, [response]);

  // 로그인 성공 시 다음 화면으로 이동
  useEffect(() => {
    if (userInfo) {
      router.replace("/(tabs)"); // 또는 원하는 경로로 변경
    }
  }, [userInfo]);

  return (
    <SafeAreaView style={styles.safeArea} edges={['top', 'bottom', 'left', 'right']}>
      <StatusBar barStyle="light-content" backgroundColor="#000" />
      <View style={styles.container}>
        <MaskedView
          maskElement={<Text style={styles.title}>Y Calendar</Text>}
          style={styles.maskedView}
        >
          <LinearGradient
            colors={["#B18AFF", "#F7C873"]}
            start={{ x: 0, y: 0 }}
            end={{ x: 1, y: 0 }}
            style={styles.gradient}
          />
        </MaskedView>
        <View style={styles.bottomContainer}>
          <TouchableOpacity 
            style={[styles.googleButton, !request && styles.disabledButton]} 
            activeOpacity={0.8}
            onPress={() => promptAsync()}
            disabled={!request}
          >
            <Image
              source={require('../../assets/images/google-logo.png')}
              style={styles.googleIcon}
              resizeMode="contain"
            />
            <Text style={styles.googleButtonText}>
              Google로 로그인하기
            </Text>
          </TouchableOpacity>
        </View>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#000',
  },
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#000',
  },
  maskedView: {
    height: 40,
    justifyContent: 'center',
    alignItems: 'center',
    alignSelf: 'center',
    marginBottom: 0,
  },
  gradient: {
    flex: 1,
    width: 200,
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    textAlign: 'center',
    color: '#fff',
  },
  bottomContainer: {
    position: 'absolute',
    bottom: 40,
    left: 0,
    right: 0,
    alignItems: 'center',
  },
  googleButton: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#fff',
    borderRadius: 24,
    paddingVertical: 12,
    paddingHorizontal: 24,
    minWidth: 320,
    justifyContent: 'center',
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 2,
  },
  disabledButton: {
    opacity: 0.7,
  },
  googleIcon: {
    width: 24,
    height: 24,
    marginRight: 8,
  },
  googleButtonText: {
    color: '#222',
    fontSize: 16,
    fontWeight: '500',
  },
}); 