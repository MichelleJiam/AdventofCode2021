#!/usr/bin/env python3

from d09a import lowest_point
import numpy as np
from skimage.morphology import flood_fill

with open('d09.in') as f:
    heightMap = [[int(i) for i in line if i != '\n'] for line in f]
heightMap = np.array(heightMap)
lowPoints = {(row, col): line[col] for row, line in enumerate(heightMap) for col, num in enumerate(line)
             if lowest_point(heightMap, row, col) is True}
# lowPoints = {}
# for row, line in enumerate(heightMap):  # replaced by cursed dict comprehension above
#     for col, num in enumerate(line):
#         if lowest_point(heightMap, row, col) is True:
#             lowPoints[(row, col)] = line[col]
# print(lowPoints)

for point in lowPoints:
    heightMap[point[0]][point[1]] = -1
heightMap = np.where(heightMap < 9, -1, heightMap)

# for row, line in enumerate(heightMap):  # replaced by above
#     for col, num in enumerate(line):
#         # print(num)
#         # if num < 9: num = -1
#         if heightMap[row][col] < 9:
#             heightMap[row][col] = -1
# print(heightMap, "\n")

basins = []
for point in lowPoints:
    map_flooded = flood_fill(heightMap, point, 10, connectivity=1)
    basins.append(np.count_nonzero(map_flooded == 10))
basins.sort(reverse=True)
print(basins[0] * basins[1] * basins[2])
