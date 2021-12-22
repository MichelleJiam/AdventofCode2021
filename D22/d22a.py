#!/usr/bin/env python3

import re
from operator import countOf

TEST = "./test2.in"
INPUT = "./d22.in"


def within_range(x1, x2, y1, y2, z1, z2):
    return -50 <= x1 <= 50 and -50 <= x2 <= 50 and -50 <= y1 <= 50 and -50 <= y2 <= 50 and -50 <= z1 <= 50 and -50 <= z2 <= 50


if __name__ == "__main__":
    cubes = {}
    with open(INPUT) as f:
        for line in f:
            switch = 1 if "on" in line else 0
            x1, x2, y1, y2, z1, z2 = [int(num) for num in re.findall('-?\d+', line)]  # regex for positive and negative numbers
            if within_range(x1, x2, y1, y2, z1, z2) is False:
                continue
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    for z in range(z1, z2 + 1):
                        cubes[(x, y, z)] = switch
    print(countOf(cubes.values(), 1))
