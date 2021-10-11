cipher = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_jdJBFOXJ}"

decryption = ''

for letter in cipher:
    if not letter.isalpha():
        decryption += letter
    elif letter.islower():
        if ord(letter) - 13 < ord('a'):
            decryption += chr(ord('z') + ord(letter) - 12 - ord('a'))
        else:
            decryption += chr(ord(letter) - 13)
    else:
        if ord(letter) - 13 < ord('A'):
            decryption += chr(ord('Z') + ord(letter) - 12 - ord('A'))
        else:
            decryption += chr(ord(letter) - 13)

print(decryption)
