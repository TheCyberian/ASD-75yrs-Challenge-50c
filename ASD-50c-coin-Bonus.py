"""
Inner Ring Bolded Characters:
GOAMVITSNGTNEGREREAICIEALFN5LFCHDEEE7NRX5
len - 41

Outer Ring Bolded Characters:
DRFHRMVKGNVRXFFHRVXGR
URWOIRDWCWG

DRFHRMVKGNVRXFFHRVXGRURWOIRDWCWG
len - 32


Outer Ring Striped Characters:
ZLLZMGOMVL
MXRBRSV

ZLLZMGOMVLMXRBRSV
len - 17
"""
# plaintext = 'E3B8287D4290F7233814D7A47A291DC0F71B2806D1A53B311CC4B97A0E1CC2B93B31068593332F10C6A3352F14D1B27A3514D6F7382F1AD0B0322955D1B83D3801CDB2287D05C0B82A311085A033291D85A3323855D6BC333119D6FB7A3C11C4A72E3C17CCBB33290C85B6343955CCBA3B3A1CCBB62E341ACBF72E3255CAA73F2F14D1B27A341B85A3323855D6BB333055C4A53F3C55C7B22E2A10C0B97A291DC0F73E3413C3BE392819D1F73B331185A3323855CCBA2A3206D6BE3831108B'
plaintext = 'GOAMVITSNGTNEGREREAICIEALFN5LFCHDEEE7NRX5'
xor_key = 'A5D75'


def encrypt_or_decrypt_string(string, key):
    cipher_string = []
    key_itr = 0

    for x in string:
        # print("x {} : ord {} : key {}".format(x, ord(x), key[key_itr]))
        cipher_string.append(chr(ord(x) ^ ord(key[key_itr])))
        # cipher_string.append(ord(x) ^ ord(key[key_itr]))
        key_itr += 1
        if key_itr >= len(key):
            key_itr = 0
    # print("".join(cipher_string))
    return repr("".join(cipher_string))

# print(xor_key*76 + 'A5')
# plaintext_int = int(plaintext, 16)
plaintext_int = int(plaintext, 10)
# print((len(plaintext)//len(xor_key)))
# print(len(plaintext)%len(xor_key))
# print(xor_key[:(len(plaintext)%len(xor_key))])
key_increased_size = xor_key*(len(plaintext)//len(xor_key)) + xor_key[:(len(plaintext)%len(xor_key))] 

# key_int = int(xor_key*76 + 'A5', 16) 
# key_int = int(key_increased_size, 16) 
key_int = int(key_increased_size, 10) 

# print("Int Value of Text: ",plaintext_int)
# print("Int Value of Key: ",key_int)
# print(plaintext_int^key_int)
xored_hex = hex(plaintext_int^key_int)
# print("XORED: ", xored_hex)
# print(codecs.decode())
print("OUTPUT: ", bytes.fromhex('%x' % (plaintext_int^key_int)).decode ('utf-8'))