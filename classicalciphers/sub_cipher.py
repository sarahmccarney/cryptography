import random

def encrypt(plaintext, key):
    alphabet_str = 'abcdefghijklmnopqrstuvwxyz'
    plaintext = plaintext.lower()
    ciphertext = ''
    for i in range(len(plaintext)):
        try: 
            index = str.index(alphabet_str, plaintext[i])
        except ValueError:
            pass
        else:
            ciphertext = ciphertext + key[index]
    ciphertext = " ".join(ciphertext[j: j + 5] for j in range(0, len(ciphertext), 5))
    return(ciphertext)

def decrypt(ciphertext, key):
    alphabet_str = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_list = list(alphabet_str)
    key_str = "".join(str(x) for x in key)
    plaintext = ''
    for i in range(len(ciphertext)):
        try:
            index = str.index(key_str, ciphertext[i])
        except ValueError:
            pass
        else:
            plaintext = plaintext + alphabet_list[index]
    return(plaintext)

key_1 = random.sample(list('abcdefghijklmnopqrstuvwxyz'), 26)

key_2 = ['u', 'y', 'e', 's', 'f', 'n', 'h', 'd', 'm', 'i', 'k', 'w', 'x', 'z', 'o', 'v', 'a', 'g', 't', 'j', 'q', 'b', 'c', 'p', 'l', 'r']


if __name__ == '__main__':
    print(key_1)
    print(encrypt('My name is Sarah and this is a test.', key_1))
    print(encrypt('My name is Sarah and this is a test.', key_2))
    print(decrypt('xlzux fmttu guduz sjdmt mtujf tj', key_2))

