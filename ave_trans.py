#!/usr/bin/env python

import sys

def main():
    num = 0
    accm = 0.0
    for line in sys.stdin:
        try:
            value = int(line.strip())
        except ValueError:
            continue

        num += 1
        accm += value
        print("{0:f}".format(accm/num))

if __name__ == '__main__':
    main()
