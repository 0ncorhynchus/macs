#!/usr/bin/env python3

import math
import copy
import random

import os
import sys
import time

if os.name == 'nt':
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')

class Ising:

    def copy(state):
        copied = Ising(state.L)
        copied.data = copy.copy(state.data)
        return copied

    def __init__(self, L):
        self.L = L
        self.data = [1]*(L*L)

    def validate_index(self, i, j):
        return (i % self.L, j % self.L)

    def at(self, i, j):
        # Periodic Bondary Condition
        i, j = self.validate_index(i, j)
        return self.data[i * self.L + j]

    def swap(self, i, j):
        i, j = self.validate_index(i, j)
        self.data[i * self.L + j] *= -1

    def to_string(self):
        return "\n".join(" ".join(
            map(lambda x: "o" if x == 1 else " ",
                self.data[i*self.L:(i+1)*self.L]))
            for i in range(self.L))

def calc_r(theta, state, i, j):
    # (i, j) : Coordinate to swap
    return math.exp(-2 * theta * state.at(i,j) * (
        state.at(i-1,   j) +
        state.at(i+1,   j) +
        state.at(  i, j-1) +
        state.at(  i, j+1)))

def step(theta, state, i, j):
    if random.random() < calc_r(theta, state, i, j):
        state.swap(i, j)

def cycle_index(L, i, j):
    return (math.floor(random.random() * L),
            math.floor(random.random() * L))

def print_state(step, state):
    clear()
    print("{0:05d}\n{1}".format(step, state.to_string()))

def get_args(L, theta):
    argc = len(sys.argv)
    try:
        if argc > 2:
            L = int(sys.argv[1])
            theta = float(sys.argv[2])
        elif argc == 2:
            L = int(sys.argv[1])
    except ValueError:
        pass
    return (L, theta)

def main():
    L, theta = get_args(8, 0.2)

    num_step = 10000
    state = Ising(L)
    i, j = 0, 0
    try:
        for n in range(num_step):
            i, j = cycle_index(state.L, i, j)
            step(theta, state, i, j)
            print_state(n, state)
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("") # finalize console

if __name__ == '__main__':
    main()
