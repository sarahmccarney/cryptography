from shift_cipher import encrypt
from matplotlib import pyplot as plt

message = '''Cryptography, or cryptology is the practice and study of techniques
for secure communication in the presence of adversarial behavior. More generally, 
cryptography is about constructing and analyzing protocols that prevent third parties 
or the public from reading private messages. Modern cryptography exists at the 
intersection of the disciplines of mathematics, computer science, information security, 
electrical engineering, digital signal processing, physics, and others. Core concepts 
related to information security (data confidentiality, data integrity, authentication, 
and non-repudiation) are also central to cryptography. Practical applications of 
cryptography include electronic commerce, chip-based payment cards, digital currencies, 
computer passwords, and military communications.'''

code = encrypt(message, 7).lower()

def counter(ciphertext):
    '''
    Determine frequency of each letter in an extract.

    Args:
    ciphertext(str) : Extract for which letter frequency is to be found.
    
    Return:
    list: List of frequencies of each letter.
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    count = []
    
    for letter in alphabet:
        count.append(ciphertext.count(letter))

    modified_count = []
    
    for i in count:
        modified_count.append(round(i/sum(count), 3))

    return modified_count

#plotting comparsion graphs
letter_freq = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002, 0.008, 0.040, 0.024, 0.067, 0.075, 0.019,
               0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.024, 0.002, 0.020, 0.007] #from wikipedia

alphabet ='abcdefghijklmnopqrstuvwxyz'
alphabet_list = list(alphabet)

modified_count = counter(code)

if __name__ == '__main__':
    fig, ax = plt.subplots(1, 2)
    ax1 = ax[0]
    ax1.bar(alphabet_list, letter_freq)
    ax1.set_title('Letter Frequencies in English text')
    ax1.set_xlabel('Letters')
    ax1.set_ylabel('Frequency')

    ax2 = ax[1]
    ax2.bar(alphabet_list, modified_count)
    ax2.set_title('Letter Frequencies in encripted text')
    ax2.set_xlabel('Letters')
    ax2.set_ylabel('Frequency')
    ax2.sharey(ax1)

    plt.show()

def basic_decrypt(ciphertext):
    '''
    Find most common letter in ciphertext and map it to e to guess shift.

    Args:
    ciphertext(str): Text to be decrypted.

    Returns:
    int: Shift.
    '''
    modified_count = counter(ciphertext)

    n0 = max(modified_count)
     
    i = modified_count.index(n0)

    if i < 4:
        shift = 25 - i 
    
    if i >= 4:
        shift = i - 4 
    return(shift)

#advanced decryption function - returns shift with lowest chi squared value
def advanced_decrypt(ciphertext):
    '''
    Return shift with lowest chi squared value.

    Args:
    ciphertext(str): Text to be decrypted.

    Returns:
    int: Shift.
    '''
    modified_count = counter(ciphertext)

    letter_freq = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.020, 0.061, 0.070, 0.002, 0.008, 0.040, 0.024, 0.067, 0.075, 0.019, 
                   0.001, 0.060, 0.063, 0.091, 0.028, 0.010, 0.024, 0.002, 0.020, 0.001]

    chi_squared_list = []
    for shift in range(26):
        chi_squared_val = 0
        for ii in range(26):
            expected = letter_freq[ii]
            observed = modified_count[(ii + shift) % 26]
            chi_squared_val += ((observed - expected)**2)/ expected 
        chi_squared_list.append(chi_squared_val)
    
    return chi_squared_list.index(min(chi_squared_list))
     

if __name__ == '__main__':
    print(basic_decrypt(code))
    print(advanced_decrypt(code))

