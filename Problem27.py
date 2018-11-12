"""
Euler discovered the remarkable quadratic formula:

n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.
"""

def check(num):
    for nn in range(2,int(num/2)):
        if num%nn == 0:
            return False
    return True
def prime(c,d):
    count = 0
    for n in range(0,80):
        flag = check(n*n+c*n+d)
        if flag:
            count = count + 1
        else:
            return count
    return count
def equation_formming():
    return_count = 0
    max = 0
    dic = {}
    for a in range(-100,2000):
        for b in range(-100,2000):
            return_count = prime(a,b)
            if return_count > max:
                max = return_count
                dic[a] = b
    return dic
if __name__ == '__main__':
    dic_local = equation_formming()
    print(dic_local)
