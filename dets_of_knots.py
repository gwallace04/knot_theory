# Author: Gabriel Wallace <wallace004@live.missouristate.edu>

import csv
import math

def main():
    with open("knot_det.txt") as f:
        contents = f.read().split(',')
        contents = list(map(int, contents))
    hist_of_dets = count_elements(contents)
    with open("Determinants of knots.csv", "w") as f:
        w = csv.writer(f)
        w.writerows(hist_of_dets.items())
    prime_list = list()
    for num in contents:
        prime_set = unique_prime_factors(num)
        for p in prime_set:
            prime_list.append(p)
    hist_of_primes = count_elements(prime_list)
    with open("Prime Dets.csv", "w") as f:
        w = csv.writer(f)
        w.writerows(hist_of_primes.items())

    
def count_elements(seq):
    hist = dict()
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
    return hist

def unique_prime_factors(n):
    factors = list()
    for i in range(3, n + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n / i
    return set(factors)

if __name__ == '__main__':
    main()
