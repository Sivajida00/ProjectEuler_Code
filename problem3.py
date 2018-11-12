"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""
import math
def check(num):
    for i in range(2, num / 2):
        if num % i == 0:
            return False
    return True
for num in range(int(600851475143/2),1,-1):
    if 600851475143%num == 0:
        flag = check(num)
        if flag:
            print(num)
            break

