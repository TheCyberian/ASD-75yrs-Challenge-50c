import morse_code


BINARY_CODE = "1000001101001110001001000011110001011100100110010011000001100100110010"

# Spliting  into 7-bit chunks for ASCII conversion.
char_list = [BINARY_CODE[i:i+7] for i in range(0, len(BINARY_CODE), 7)]
print("Ascii text: ")
for char in char_list:
    n = int(char, 2)
    print(chr(n), end='')

MORSE_CODE = ".---- ----. ....- --...  -.. ... -... .- .-.. -... . .-. - .--. .- .-. -.-"

print("\nMorse decoded: ")
print(morse_code.decode(MORSE_CODE))
