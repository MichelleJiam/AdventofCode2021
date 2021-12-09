#!/usr/bin/env python3

from d09a import lowest_point
import numpy as np
from skimage.morphology import flood_fill

with open('d09.in') as f:
    heightMap = [[int(i) for i in line if i != '\n'] for line in f]
heightMap = np.array(heightMap)

lowPoints = [(row, col) for row in range(len(heightMap)) for col in range(len(heightMap[0]))
             if lowest_point(heightMap, row, col) is True]

for r, c in lowPoints:
    heightMap[r][c] = -1
heightMap = np.where(heightMap < 9, -1, heightMap)  # masking low points

basins = []
for r, c in lowPoints:
    map_flooded = flood_fill(heightMap, (r, c), 10, connectivity=1)
    basins.append(np.count_nonzero(map_flooded == 10))
basins.sort(reverse=True)
print(basins[0] * basins[1] * basins[2])
