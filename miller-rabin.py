from math import gcd
import random

def miller_rabin(n, a):
    '''Tests whether an integer a is a witness for (the compositeness of) an integer n'''
    if not n % 2:
        return "Composite"
    if gcd(a, n) != 1:
        if gcd(a, n) < n:
            return "Composite"
        
    k = 1
    while (n-1) % 2**k == 0:
        k += 1

    k -= 1

    q = int((n-1)/(2**k))
    new_a = pow(a, q, n)
    a = new_a

    if a % n == 1:
        return "Fails"

    i = 0
    while i <= k:
        if a % n == (n-1):
            return "Fails"

        a = (a**2) % n
        i += 1

    return "Composite" 

def PrimeTest(p):
    '''Uses the Miller-Rabin test to determine whether an integer p is prime '''
    a_values = random.sample(range(p), 100)
    for i in range(100):
        if miller_rabin(p, int(a_values[i])) == 'Composite':
            return 'Not Prime'

    return('Likely a prime') 


if __name__ == "__main__" :
    # print(miller_rabin(561, 2))
    # print(miller_rabin(172947529, 17))
    # print(miller_rabin(172947529, 3))
    # print(miller_rabin(172947529, 23))

    print(PrimeTest(172947529))
    print(PrimeTest(479001599))
    print(PrimeTest(87178291199))


