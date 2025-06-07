import * as Google from 'expo-auth-session/providers/google';
import * as WebBrowser from 'expo-web-browser';
import { useEffect } from 'react';

WebBrowser.maybeCompleteAuthSession();

export function useGoogleAuth() {
  const [request, response, promptAsync] = Google.useAuthRequest({
    iosClientId: process.env.EXPO_PUBLIC_GOOGLE_IOS_ID,
    androidClientId: process.env.EXPO_PUBLIC_GOOGLE_ANDROID_ID,
    webClientId: process.env.EXPO_PUBLIC_GOOGLE_WEB_ID,
    usePKCE: true,
    responseType: 'token',
  });

  useEffect(() => {
    if (response?.type === 'success') {
      const { access_token } = response.params;
      // TODO: access_token을 백엔드로 POST하는 로직만 추가 -> 토큰 교환
      // 예시: fetch('/auth/google', { method: 'POST', body: JSON.stringify({ access_token }) })
    }
  }, [response]);

  return { promptAsync, request };
} 