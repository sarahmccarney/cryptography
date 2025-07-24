import numpy as np
import math

def IsPrime(n):
    ''' Return whether a number n is prime or not.'''
    if type(n) is not int:
        return False
    
    if n <= 1:
        return False
    
    for k in range(2, math.floor(np.sqrt(n) + 1)):
        if n % k == 0:
            return False
    
    return True


def primitive_roots(p):
    ''' Return a list of primitive roots for a prime number p.'''
    if IsPrime(p):
        prim_roots = []
        for k in range(1, p):
            powers = set()
            for j in range(0, p-1):
                power = (k**j) % p
                powers.add(power)
            
            if len(powers) == p-1:
                prim_roots.append(k)

        return(prim_roots)
    
    return 'Input is not valid'

print(primitive_roots(229))
print(len(primitive_roots(229)))

from gcdmethod import gcd

def eulerphi(n):
    ''' Calculate Euler's phi function for a number n.'''
    num_list = []
    for i in range(1, n):
        if gcd(i, n)[0] == 1:
            num_list.append(i)

    return(len(num_list))

print(eulerphi(228))

my_list = []
for n in range(1, 101):
    if IsPrime(n):
        if 2 in primitive_roots(n):
            my_list.append(n)
        
print(my_list)


