import math
from gcdmethod import gcd

def relatively_prime(a, b):
    if a == b:
        if a == 1:
            return True
        else:
            return False
    if math.gcd(a, b) == 1:
        return True
    else:
        return False
    
# if __name__ == '__main__':
#     print(relatively_prime(1, 7))
#     print(relatively_prime(1, 0))
#     print(relatively_prime(2, 0))
#     print(relatively_prime(12, 35))
#     print(relatively_prime(18, 42))

def pairwise_relatively_prime(int_list):
    for i in range(len(int_list) - 1):
        for j in range(i+1, len(int_list)):
            if not relatively_prime(int_list[i], int_list[j]):
                return False
            
    return True

# if __name__ == '__main__':
#     print(pairwise_relatively_prime([2, 3, 5]))
#     print(pairwise_relatively_prime([2, 3, 4]))
#     print(pairwise_relatively_prime([2, 5, 7, 9, 11, 17]))
#     print(pairwise_relatively_prime([2, 3, 5, 7, 9, 11, 17]))

def chinese_remainder_simple(a, m, b, n):
    if not relatively_prime(m,n):
      return 'Invalid input: m and n must be relatively prime'  
    inv_m = gcd(m, n)[1]
    y = inv_m*(b-a) % n
    x = a + m*y
    return x

# if __name__ == '__main__':
#     print(chinese_remainder_simple(1, 5, 9, 11))


def chinese_remainder(int_list, m_list):
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
    print(chinese_remainder([2, 3, 4], [3, 7, 16]))

    

    
