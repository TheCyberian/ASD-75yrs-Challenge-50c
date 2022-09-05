encrypted_string = "DVZIVZFWZXRLFHRMXLMXVKGZMWNVGRXFOLFHRMVCVXFGRLM"


# Atbash Cipher
# WEAREAUDACIOUSINCONCEPTANDMETICULOUSINEXECUTION
def atbash_cipher(cipher_text):
    a_z = list(map(lambda x:chr(x), range(ord('A'), ord('Z')+1)))
    z_a = sorted(a_z, reverse=True)
    conversion_table = dict(zip(a_z, z_a))
    # print("conversion_table: ", conversion_table)
    char_list = list()
    for char in cipher_text:
        try:
            char_list.append(conversion_table[char])
        except KeyError:
            char_list.append(char)
    return ''.join(char_list)

print("decrypted_text: ", atbash_cipher(encrypted_string))
