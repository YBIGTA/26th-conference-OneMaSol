import { makeRedirectUri } from 'expo-auth-session';
import * as Google from 'expo-auth-session/providers/google';
import * as WebBrowser from 'expo-web-browser';
import { useEffect } from 'react';
import { Alert, Platform } from 'react-native';
import { useAuth } from '../app/context/AuthContext'; // signIn 훅 사용

WebBrowser.maybeCompleteAuthSession();

// iOS·Android용 네이티브 스키마 (Google 콘솔에서 복사)
const IOS_SCHEME =
  'com.googleusercontent.apps.237218242314-1sbhr99ed8d3rmt12a1pbr7fum0d6po4:/oauthredirect';
const ANDROID_SCHEME =
  'com.googleusercontent.apps.237218242314-7dairoo5vmjvd4nup11dpajt2bfqjueg:/oauthredirect';

export function useGoogleAuth() {
  const { signIn } = useAuth();

  const redirectUri = makeRedirectUri({
    native: Platform.select({ ios: IOS_SCHEME, android: ANDROID_SCHEME }),
    useProxy: true,       // Expo Go·dev-client일 때 true
  });

  const [request, response, promptAsync] = Google.useAuthRequest({
    iosClientId: process.env.EXPO_PUBLIC_GOOGLE_IOS_ID,
    androidClientId: process.env.EXPO_PUBLIC_GOOGLE_ANDROID_ID,
    webClientId: process.env.EXPO_PUBLIC_GOOGLE_WEB_ID,
    scopes: ['openid', 'profile', 'email'],
    usePKCE: true,
    responseType: 'id_token',  // id_token만 사용하도록 변경
    redirectUri,          // ★ 반드시 명시
  });

  useEffect(() => {
    if (response?.type === 'success') {
      const { id_token } = response.params;  // id_token 사용
      // 백엔드와 JWT 교환
      signIn(id_token).catch(err =>
        Alert.alert('로그인 실패', err.message ?? '알 수 없는 오류'),
      );
    } else if (response?.type === 'error') {
      Alert.alert('Google 로그인 실패', response.error?.message ?? '취소됨');
    }
  }, [response]);

  return { promptAsync, request };
}
