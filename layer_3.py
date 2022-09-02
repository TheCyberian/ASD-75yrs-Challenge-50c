"""
Columnar Transposition Cipher
------------------------------
7 Width x 5 Depth
BGOAMVO 
EIATSIR 
LNGTTNE 
OGRERGX 
NTEAIFC 

ECAIEOA 
LEKFNR5 
LWEFCHD 
EEAEEE7 
NMDRXX5
"""
cipher_text = "BGOAMVOEIATSIRLNGTTNEOGRERGXNTEAIFCECAIEOALEKFNR5LWEFCHDEEAEEE7NMDRXX5"

def calculateTransposition7x5(s):
    strings = []
    for j in range(7):
        for i in range(5):
            # print(s[i*7+j])
            strings.append(s[i*7+j])

    print("".join(strings))


# BELONGING TO A GREAT TEAM STRIVING FOR EXCELLENCE WE MAKE A DIFFERENCE XOR HEX A5D75
calculateTransposition7x5(cipher_text[:35])
calculateTransposition7x5(cipher_text[35:])
