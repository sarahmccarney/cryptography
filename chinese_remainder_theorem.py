import math
from gcdmethod import gcd

def relatively_prime(a, b):
    '''Determine whether 2 numbers are relatively prime'''
    if a == b:
        if a == 1:
            return True
        else:
            return False
    if math.gcd(a, b) == 1:
        return True
    else:
        return False

def pairwise_relatively_prime(int_list):
    '''Determine whether a list contains pairwise relatively prime entries'''
    for i in range(len(int_list) - 1):
        for j in range(i+1, len(int_list)):
            if not relatively_prime(int_list[i], int_list[j]):
                return False
            
    return True

def chinese_remainder_simple(a, m, b, n):
    '''
    Solve a system of two congruences using the Chinese Remainder Theorem:
        x ≡ a (mod m)
        x ≡ b (mod n).
    
    Args:
    a (int): Remainder of the first congruence.
    m (int): Modulus of the first congruence.
    b (int): Remainder of the second congruence.
    n (int): Modulus of the second congruence.
    
    Returns:
    int: The smallest non-negative solution x that satisfies both congruences.
         Returns a string error message if m and n are not relatively prime.'''
    
    if not relatively_prime(m,n):
      return 'Invalid input: m and n must be relatively prime'  
    inv_m = gcd(m, n)[1]
    y = inv_m*(b-a) % n
    x = a + m*y
    return x


def chinese_remainder(int_list, m_list):
    '''
    Solve a system of simultaneous congruences using the Chinese Remainder Theorem:
        x ≡ int_list[i] (mod m_list[i]) for all i.
    
    Args:
    int_list (list of int): List of remainders.
    m_list (list of int): List of moduli.
    
    Returns:
    int: The smallest non-negative solution x that satisfies all the congruences.
         Returns a string error message if the moduli are not pairwise relatively prime.
    '''
    
    if not(pairwise_relatively_prime(m_list)):
        return 'Invalid input: m_list must be pairwise relatively prime'
    
    c = chinese_remainder_simple(int_list[0], m_list[0], int_list[1], m_list[1])
    m_product = m_list[0]*m_list[1]
    for i in range(2, len(int_list)):
        c1 = chinese_remainder_simple(c, m_product, int_list[i], m_list[i])
        m_product *= m_list[i]
        c = c1

    return c

if __name__ == '__main__':
    print(relatively_prime(12, 35))
    print(relatively_prime(18, 42))
    print(pairwise_relatively_prime([2, 5, 7, 9, 11, 17]))
    print(pairwise_relatively_prime([2, 3, 5, 7, 9, 11, 17]))
    print(chinese_remainder_simple(1, 5, 9, 11))
    print(chinese_remainder([2, 3, 4], [3, 7, 16]))

    

    
