from math import gcd
import random

def miller_rabin(n, a):
    '''Tests whether an integer 'a' is a witness for (the compositeness of)
        an integer 'n' '''
    if n % 2 == 0:
        return "Composite"
    if 1 < gcd(a, n) < n:
            return "Composite"

    k = 0
    q = n - 1
    while q % 2 == 0:
        q //= 2
        k += 1

    x = pow(a, q, n)
    
    if x == 1 or x == (n-1):
        return "Fails"

    for _ in range(k - 1):
        x = pow(x, 2, n)
        if x == n - 1:
            return "Fails"

    return "Composite" 

def PrimeTest(p):
    '''Uses the Miller-Rabin test to determine whether an integer 'p' is prime '''
    a_values = [random.randrange(2, p-1) for _ in range(100)]
    for i in range(100):
        if miller_rabin(p, int(a_values[i])) == 'Composite':
            return False

    return True

def GeneratePrimes(power, r):
    '''
    Generate a list of integers `j` in the range [0, 1000] such that the 
    number N = 2310 * (2^power + j) + r is likely to be a prime.

    Args:
    power (int): The exponent used in the expression 2^power which will 
                determine how large the primes are.
    
    rel_prime (int): The constant added after multiplying by 2310, which 
                    should be relatively prime to 2310 (2*3*5*7*11) to 
                    increase chances of primality.

    Returns:
    list of int: A list of all integers j in [0, 1000] for which 
    N = 2310 * (2^power + j) + r is likely prime.
    '''

    j_list = []
    for j in range(1001):
        K = 2**power + j
        N = 2310*K + r
        if PrimeTest(N):
            j_list.append(j)
    return j_list
    

if __name__ == "__main__" :
    # print(miller_rabin(561, 2))
    # print(miller_rabin(172947529, 17))
    # print(miller_rabin(172947529, 3))
    # print(miller_rabin(172947529, 23))

    # print(PrimeTest(172947529))
    # print(PrimeTest(479001599))
    # print(PrimeTest(87178291199))
    
    print(GeneratePrimes(1013, 1139))