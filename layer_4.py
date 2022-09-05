plaintext = 'E3B8287D4290F7233814D7A47A291DC0F71B2806D1A53B311CC4B97A0E1CC2B93B31068593332F10C6A3352F14D1B27A3514D6F7382F1AD0B0322955D1B83D3801CDB2287D05C0B82A311085A033291D85A3323855D6BC333119D6FB7A3C11C4A72E3C17CCBB33290C85B6343955CCBA3B3A1CCBB62E341ACBF72E3255CAA73F2F14D1B27A341B85A3323855D6BB333055C4A53F3C55C7B22E2A10C0B97A291DC0F73E3413C3BE392819D1F73B331185A3323855CCBA2A3206D6BE3831108B'
xor_key = 'A5D75'

plaintext_int = int(plaintext, 16)
# key_int = int(xor_key*76 + 'A5', 16) 
padded_key = xor_key*(len(plaintext)//len(xor_key)) + xor_key[:(len(plaintext)%len(xor_key))]
key_int = int(padded_key, 16)

print("Int Value of Text: ",plaintext_int)
print("Int Value of Key: ",key_int)
xored_hex = hex(plaintext_int^key_int)
print("XORED: ", xored_hex)
# For 75 years the Australian Signals Directorate has brought together people with the skills, adaptability and imagination to operate in the slim area between the difficult and the impossible.
print("OUTPUT: ", bytes.fromhex('%x' % (plaintext_int^key_int)).decode ('utf-8'))
