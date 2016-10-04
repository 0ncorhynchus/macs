#!/usr/bin/env python

import math
import copy
import random
import sys

# Not normalized
def calc_p(b, x, y):
    return math.exp(-(x*x - 2*b*x*y + y*y)/2)

def random_delta():
    sigma = 0.5
    return (random.gauss(0.0, sigma),
            random.gauss(0.0, sigma))

def is_satisfy_condition(x, y):
    return y >= x*x/2 + 3

def step(b, x, y):
    dx, dy = random_delta()
    nx, ny = (x+dx, y+dy)

    if not is_satisfy_condition(nx, ny):
        return (x, y)

    old_p = calc_p(b, x, y)
    new_p = calc_p(b, nx, ny)

    if old_p * random.random() < new_p:
        return (nx, ny)
    return (x, y)


def main():
    num_step = 1000
    x, y = 3.0, 9.0
    b = 0.8

    print("{0:f}, {1:f}".format(x, y))
    for n in range(num_step):
        x, y = step(b, x, y)
        print("{0:f}, {1:f}".format(x, y))

if __name__ == '__main__':
    main()

