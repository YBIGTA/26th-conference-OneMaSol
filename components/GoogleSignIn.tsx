import { Button } from 'react-native';
import { useGoogleAuth } from '../hooks/useGoogleAuth';

export default function GoogleSignIn() {
  const { promptAsync, request } = useGoogleAuth();
  return (
    <Button
      title="Sign in with Google"
      disabled={!request}
      onPress={() => promptAsync()}
    />
  );
}