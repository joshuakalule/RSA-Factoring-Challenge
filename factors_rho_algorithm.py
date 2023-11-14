#!/usr/bin/env python3

'''Factorization using POLLARD’S RHO ALGORITHM'''

import random
import sys


def gcd(x, y):
    '''Find the greatest common divisor'''
    return x if y == 0 else gcd(y, x % y)


def mod_pow(base, exp, mod):
    '''
    square-and-multiply algorithm
    efficient way of calculating: a^b mod M
    '''
    res = 1
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        exp >>= 1
        base = (base * base) % mod
    return res


def poll_rho(n):
    '''POLLARD’S RHO ALGORITHM'''
    if n == 1:
        return n

    if n % 2 == 0:
        return 2

    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1

    while d == 1:
        x = (mod_pow(x, 2, n) + c + n) % n
        y = (mod_pow(y, 2, n) + c + n) % n
        y = (mod_pow(y, 2, n) + c + n) % n
        d = gcd(abs(x - y), n)

        if d == n:
            return poll_rho(n)

    return d


def main():
    ''' entry point'''
    if len(sys.argv) != 2:
        sys.stderr.write("usage: factors <file>\n")
        exit(0)

    with open(sys.argv[1], 'r') as fp:
        for line in fp:
            line = line.rstrip()
            num = int(line)
            f1 = poll_rho(num)
            f2 = int(num / f1)

            print(f"{num}={f2}*{f1}")


if __name__ == "__main__":
    main()
