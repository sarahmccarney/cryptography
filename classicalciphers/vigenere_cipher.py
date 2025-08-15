import shift_cipher as s

def find_shift(keyword):
    '''
    Return length of keyword.
    May be useful for frequency analysis.
    '''
    keyword = keyword.replace(" ","")
    return len(keyword)

def v_encrypt(plaintext, keyword):
    '''
    Encrypt using a vigenere cipher through the use of a shift cipher function.

    Args:
    plaintext(str): Message to encrypt.
    keyword(str): Keywrod used to encrypt message.

    Returns: 
    str: Encrypted message.
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    plaintext = plaintext.replace(" ", "")
    plaintext = plaintext.lower()
    keyword = keyword.replace(" ","")
    ciphertext = ''
    for i in range(len(plaintext)):
        for j in range(26):
            if keyword[i % (len(keyword))] == alphabet[j]:
                ciphertext += s.encrypt(plaintext[i], j)
    ciphertext = " ".join(ciphertext[i : i + 5] for i in range(0, len(ciphertext), 5))
    return ciphertext  

def v_decrypt(ciphertext, keyword):
    '''
    Decrypt using a vigenere cipher through the use of a shift cipher function.

    Args:
    ciphertext(str): Code to decrypt.
    keyword(str): Keywrod used to decrypt message.

    Returns: 
    str: Decrypted message.
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ciphertext = ciphertext.replace(" ", "")
    ciphertext = ciphertext.lower()
    keyword = keyword.replace(" ","")
    plaintext = ''
    for i in range(len(ciphertext)):
        for j in range(26):
            if keyword[i % (len(keyword))] == alphabet[j]:
                plaintext += s.decrypt(ciphertext[i], j)
    return plaintext

if __name__ == '__main__':
    plaintext = 'The rain in Spain stays mainly in the plain'
    keyword = 'flamingo'
    ciphertext = 'YSEDI VTWSD PMQAY HFJSY IVTZD TNFPR VZFTN'
    print(v_encrypt(plaintext, keyword))
    print(v_decrypt(ciphertext, keyword))         
            

