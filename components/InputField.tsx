import { colors } from "@/constants";
import React from "react";
import {
  StyleSheet,
  Text,
  TextInput,
  TextInputProps,
  View,
} from "react-native";

interface InputFieldProps extends TextInputProps {
  label: string;
  variant: "filled" | "standard" | "outlined";
}

function InputField({ label, variant = "filled", ...props }: InputFieldProps) {
  return (
    <View>
      {label && <Text style={[styles.label, styles[variant]]}>{label}</Text>}
      <View style={styles.container}>
        <TextInput
          placeholderTextColor={colors.GRAY_500}
          style={styles.input}
          {...props}
        />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    height: 44,
    borderRadius: 8,
    paddingHorizontal: 10,
    justifyContent: "center",
    alignItems: "center",
    flexDirection: "row",
  },
  label: {
    fontSize: 12,
    color: colors.GRAY_700,
    marginBottom: 5,
  },
  filled: {
    backgroundColor: colors.GRAY_100,
  },
  standard: {},
  outlined: {},
  input: {
    fontSize: 16,
    padding: 0,
    flex: 1,
  },
});

export default InputField;
