
def encrypt(plaintext, shift):
    '''
    Encrypt using a shift cipher.

    Args:
    plaintext(str): Message to encrypt.
    shift(int): Value to shift message by.

    Returns: 
    str: Encrypted message. 
    
    '''
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
    '''
    Decrypt code encrypted using a shift cipher.

    Args:
    ciphertext(str): Code to decrypt.
    shift(int): Shift value used in encryption.

    Returns: 
    str: Decrypted message. 
    '''
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
    '''
    Return all possible options for message encrypted by shift cipher.

    Args:
    ciphertext(str): Encypted message.

    Returns:
    list: 26 possible messages.
    '''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    possibilities = []
    for k in range(26):
        possibilities.append(decrypt(ciphertext, k))
    return(possibilities)

#testing
if __name__ ==  '__main__':
    print(encrypt('My name is Sarah and I am testing out three functions that I have just written in relation to shift ciphers.', 13))
   
    print(decrypt('ZLANZ RVFFN ENUNA QVNZG RFGVA TBHGG UERRS HAPGV BAFGU NGVUN IRWHF GJEVG GRAVA ERYNG VBAGB FUVSG PVCUR EF', 13))

    print(brute_force('ZLANZ RVFFN ENUNA QVNZG RFGVA TBHGG UERRS HAPGV BAFGU NGVUN IRWHF GJEVG GRAVA ERYNG VBAGB FUVSG PVCUR EF'))
    