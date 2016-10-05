#!/usr/bin/env python3

import math
import copy
import random
import sys

# Not normalized
def calc_p(theta, state):
    return math.exp(theta*(
        state[0] * state[1] +
        state[1] * state[2] +
        state[2] * state[0]))

def swap_state(state, idx):
    swapped_state = copy.copy(state)
    swapped_state[idx] *= -1
    return swapped_state

def step(theta, state, idx):
    new_state = swap_state(state, idx)
    old_p = calc_p(theta, state)
    new_p = calc_p(theta, new_state)

    # if new_p > old_p:
    #     return new_state
    if old_p * random.random() < new_p:
        return new_state
    return state

def cycle_index(idx):
    # return math.floor(random.random() * 3)
    return (idx + 1) % 3

def print_state(step, state):
    print("{0:5d},{1[0]:2d},{1[1]:2d},{1[2]:2d}".format(step, state))

def get_theta_from_arg(default):
    argc = len(sys.argv)
    if argc < 2:
        return default
    return float(sys.argv[1])

def main():
    theta = get_theta_from_arg(0.2)
    num_step = 10000

    state = [1, 1, 1] # Initial state
    idx = 0 # Index to swap

    for n in range(num_step):
        idx = cycle_index(idx)
        state = step(theta, state, idx)
        print_state(n, state)

if __name__ == '__main__':
    main()
