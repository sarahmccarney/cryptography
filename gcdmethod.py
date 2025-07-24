

def gcd(a, b):
    ''' When given an input of 2 integers, returns (g, u, v)
       where g is their greatest common divisor, and u and v are
       integers such that u*a + v*b = g'''
    u = 1
    g = a
    x = 0
    y = b

    if b == 0:
        return (a, 1, 0)

    while y:
        q = g // y
        t = g % y
        s = u - q*x
        u = x
        g = y
        x = s
        y = t

    v = int((g - a*u)/b)
        
    while u < 0:
        u = int(u + b/g)
        v = int(v - a/g)

    while u > 0:
        u1 = u
        v1 = v
        u = int(u - b/g)
        v = int(v + a/g)

    return (g, u1, v1)

# print(gcd(291, 252))
# print(gcd(228, 1056))
# print(gcd(163961, 167181))
# print(gcd(3892394, 239847))
# print(gcd(7, 0))
# print(gcd(34, 541))
# print(gcd(2, 3))