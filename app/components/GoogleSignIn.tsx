import * as Google from 'expo-auth-session/providers/google';
import * as WebBrowser from 'expo-web-browser';
import { useEffect } from 'react';
import { Alert, Button } from 'react-native';
import { useAuth } from '../context/AuthContext';

WebBrowser.maybeCompleteAuthSession();

export default function GoogleSignIn() {
  const { signIn } = useAuth();
  const [request, response, promptAsync] = Google.useAuthRequest({
    androidClientId: '237218242314-7dairoo5vmjvd4nup11dpajt2bfqjueg.apps.googleusercontent.com',
    iosClientId: '237218242314-1sbhr99ed8d3rmt12a1pbr7fum0d6po4.apps.googleusercontent.com',
  });

  useEffect(() => {
    if (response?.type === 'success') {
      const { authentication } = response;
      if (authentication?.accessToken) {
        signIn(authentication.accessToken).catch((error) => {
          Alert.alert('로그인 실패', '로그인 중 오류가 발생했습니다.');
          console.error('Sign in error:', error);
        });
      }
    }
  }, [response, signIn]);

  return (
    <Button
      disabled={!request}
      title="Google로 로그인"
      onPress={() => {
        promptAsync();
      }}
    />
  );
}