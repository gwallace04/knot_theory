# Author: Gabriel Wallace <wallace004@live.missouristate.edu>

import csv
import math

def main():
    with open("knot_det.txt") as f:
        contents = f.read().split(',')
        contents = list(map(int, contents))
    hist_of_dets = count_elements(contents)
    write_to_csv("Determinants of knots.csv", hist_of_dets)
    
def count_elements(seq):
    hist = dict()
    for i in seq:
        hist[i] = hist.get(i, 0) + 1
    return hist

def write_to_csv(file_name, some_dict):
    with open("file_name", "w") as f:
        w = csv.writer(f)
        w.writerows(some_dict.items())

def unique_prime_factors(n):
    factors = list()
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n / i
    return set(factors)


if __name__ == '__main__':
    main()
