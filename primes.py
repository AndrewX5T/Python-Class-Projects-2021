# Andrew Hein
# Advanced Programming Week 3
# primes
# 2021/2/7

import sys

userArgs = sys.argv[1:]


def isPrime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


for i in range(int(userArgs[0]), 1, -1):
    if isPrime(i):
        print(f'{i}\tPRIME')
    else:
        print(f'{i}\tCOMPOSITE')
