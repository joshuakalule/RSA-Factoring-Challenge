#!/usr/bin/env python3

"""Factorize as many numbers as possible into a product of two smaller numbers."""


import sys


def get_factors(number):
    """Return 2 factors of number."""
    divisor = 2
    while (True):
        mod = number % divisor
        if (mod == 0):
            factor1 = number / divisor
            factor2 = divisor
            return (factor1, factor2)
        divisor += 1


def main():
    """Entry point to the program."""
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: factors <file>\n")
        exit(0)

    with open(sys.argv[1], "r") as f:
        for line in f:
            number = int(line)
            factors = get_factors(number)
            print("{}={}*{}".format(number, factors[0], factors[1]))


if __name__ == "__main__":
    main()
