
def encrypt(plaintext, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ciphertext = ''
    plaintext = plaintext.lower()
    for i in range(0, len(plaintext)):
        try: 
            index = str.index(alphabet, plaintext[i])
        except ValueError:
            pass
        else:
            ii = index + shift
            if ii < 26:
                pass
            else:
                ii = ii - 26
            ciphertext = ciphertext + str(alphabet[ii])
    ciphertext = " ".join(ciphertext[i : i + 5] for i in range(0, len(ciphertext), 5))
    ciphertext = ciphertext.upper()
    return ciphertext


def decrypt(ciphertext, shift):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    plaintext = ''
    ciphertext = ciphertext.upper()
    for i in range(0, len(ciphertext)):
        try: 
            index = str.index(alphabet, ciphertext[i])
        except ValueError:
            pass
        else:
            ii = index - shift
            if ii >= 0:
                pass
            else:
                ii = 26 + ii
            plaintext = plaintext + str(alphabet[ii])
    plaintext = plaintext.lower()
    return plaintext


def brute_force(ciphertext):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    possibilities = []
    for k in range(26):
        possibilities.append(decrypt(ciphertext, k))
    return(possibilities)

if __name__ ==  '__main__':
    print(encrypt('My name is Sarah and I am testing out three functions that I have just written in relation to shift ciphers.', 13))
   
    print(decrypt('ZLANZ RVFFN ENUNA QVNZG RFGVA TBHGG UERRS HAPGV BAFGU NGVUN IRWHF GJEVG GRAVA ERYNG VBAGB FUVSG PVCUR EF', 13))

    print(brute_force('ZLANZ RVFFN ENUNA QVNZG RFGVA TBHGG UERRS HAPGV BAFGU NGVUN IRWHF GJEVG GRAVA ERYNG VBAGB FUVSG PVCUR EF'))
    