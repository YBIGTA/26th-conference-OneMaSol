// app.config.js
import 'dotenv/config';

export default {
  expo: {
    name: 'community',
    slug: 'community',
    version: '1.0.0',
    orientation: 'portrait',
    icon: './assets/images/icon.png',
    scheme: 'com.onemasol.community',
    userInterfaceStyle: 'dark',
    newArchEnabled: true,
    ios: {
      supportsTablet: true,
      bundleIdentifier: 'com.OneMaSol.OneMaSol',
      infoPlist: { UIStatusBarStyle: 'UIStatusBarStyleLightContent' },
    },
    android: {
      package: 'com.OneMaSol.OneMaSol',
      adaptiveIcon: {
        foregroundImage: './assets/images/adaptive-icon.png',
        backgroundColor: '#ffffff',
      },
      edgeToEdgeEnabled: true,
      statusBar: { backgroundColor: '#000000', barStyle: 'light-content' },
    },
    web: {
      bundler: 'metro',
      output: 'static',
      favicon: './assets/images/favicon.png',
    },
    plugins: [
      'expo-router',
      ['expo-splash-screen', {
        image: './assets/images/splash-icon.png',
        imageWidth: 200,
        resizeMode: 'contain',
        backgroundColor: '#000000',
      }],
      'expo-web-browser',
    ],
    experiments: { typedRoutes: true },
    owner: 'joseph44',
    extra: {
      router: {},
      eas: { projectId: process.env.EAS_PROJECT_ID },
      googleClientId: {
        android: process.env.EXPO_PUBLIC_GOOGLE_ANDROID_ID,
        ios: process.env.EXPO_PUBLIC_GOOGLE_IOS_ID,
        web: process.env.EXPO_PUBLIC_GOOGLE_WEB_ID,
      },
      apiUrl: process.env.EXPO_PUBLIC_API_URL,
    },
  },
};
