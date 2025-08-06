from shift_cipher import encrypt
from shift_freq_analysis import basic_decrypt, advanced_decrypt
from numpy import random
import os

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, 'study_in_scarlett.txt')


def shift_freq_test(decrypt_func, num):
    '''
    Test a decryption function using a given text file, prints number of successes
    and failures from 100 trials, for each time the test is run

    Args:
    decrypt_func(func): decryption function which takes a ciphertext and returns a guess for the shift.
    num(int): number of times for which test is to be run.

    Returns:
    None
    '''
    for n in range(1, num+1):
        Success = 0
        Failure = 0
        with open(file_path, 'r') as f:
            while Success + Failure < 100:
                f_contents = f.read(2000)
                real_key = random.randint(0, 25)
                code = encrypt(f_contents, real_key).lower()
                guess_key = decrypt_func(code)
                if real_key == guess_key:
                    Success += 1
                else:
                    Failure += 1
        print(f'{decrypt_func.__name__}: {n} - {Success} successes, {Failure} failures')

if __name__ == '__main__':
    shift_freq_test(basic_decrypt, 3)
    print()
    shift_freq_test(advanced_decrypt, 3)




