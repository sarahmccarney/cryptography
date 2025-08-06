from sub_cipher import encrypt
from shift_freq_analysis import counter
import random

message = '''In cryptography, a substitution cipher is a method of encrypting in which units of plaintext are replaced 
with the ciphertext, in a defined manner, with the help of a key; the units may be single letters (the most common), 
pairs of letters, triplets of letters, mixtures of the above, and so forth. The receiver deciphers the text by performing 
the inverse substitution process to extract the original message. Substitution ciphers can be compared with transposition 
ciphers. In a transposition cipher, the units of the plaintext are rearranged in a different and usually quite complex order, 
but the units themselves are left unchanged. By contrast, in a substitution cipher, the units of the plaintext are retained in 
the same sequence in the ciphertext, but the units themselves are altered. There are a number of different types of substitution 
cipher. If the cipher operates on single letters, it is termed a simple substitution cipher; a cipher that operates on larger 
groups of letters is termed polygraphic. A monoalphabetic cipher uses fixed substitution over the entire message, whereas a 
polyalphabetic cipher uses a number of substitutions at different positions in the message, where a unit from the plaintext is 
mapped to one of several possibilities in the ciphertext and vice versa.The first ever published description of how to crack 
simple substitution ciphers was given by Al-Kindi in A Manuscript on Deciphering Cryptographic Messages written around 850 AD. 
The method he described is now known as frequency analysis.'''

alphabet = 'abcdefghijklmnopqrstuvwxyz'

key = ['y', 'j', 'u', 'o', 'n', 't', 'f', 'b', 'd', 'e', 'w', 'q', 'a', 'l', 'z', 'k', 'g', 
        'm', 's', 'v', 'i', 'x', 'p', 'c', 'h', 'r'] #key generated randomly

code = encrypt(message, key)

letter_freq = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002, 0.008, 0.040, 0.024, 0.067, 0.075, 0.019,
               0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.024, 0.002, 0.020, 0.001] #letter frequencies taken from wikipedia

nums = range(26, 0, -1)

def number_freq(num_list):
    '''
    Assign a rank to each number in a list based on their value, highest number will have a rank of 1.

    Args:
    num_list(list): List of numbers

    Returns:
    list: List of ranks of each number in inputed list.
    '''
    nums = range(len(num_list), 0, -1)
    for num in nums:
        min_val = min(num_list)
        index = num_list.index(min_val)
        num_list[index] = num
    return num_list 

modified_count = counter(code)

def guess_key(ciphertext):
    '''
    Return a guess of key used in text encrypted by simple substitution cipher, based on letter frequencies.

    Args:
    ciphertext(str): Text which has been encrypted

    Returns:
    list: Guess of key used for encryption.
    '''
    guess_key = list(alphabet)
    for i in range(26):
        for j in range(26):
            if modified_count[i] == letter_freq[j]:
                guess_key[j] = alphabet[i]
    return guess_key

def find_matches(key, guess):
    '''
    Return exact and close matches when given a key and a guess.

    Args:
    key(list): Actual key used for simple substitution cipher.
    guess(list): Guess of key used.

    Returns:
    tuple: (Exact matches, Close matches)

    '''
    exact_matches = 0
    near_matches = 0
    for i in range(26):
        if key[i] == guess[i]:
            exact_matches += 1
        elif key[i] == guess[(i+1) % 26] or key[i] == guess[(i-1) %26]:
            near_matches += 1
    return exact_matches, near_matches

if __name__ == '__main__':
    print(number_freq(letter_freq))
    print(number_freq(modified_count)) 
    print(key)
    print(guess_key(code))
    print(find_matches(key, guess_key(code)))






