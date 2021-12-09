#!/usr/bin/env python3

def lowest_point(heightMap, row, col):
    if row > 0 and heightMap[row - 1][col] <= heightMap[row][col]:  # up
        return False
    if col > 0 and heightMap[row][col - 1] <= heightMap[row][col]:  # left
        return False
    if row < len(heightMap) - 1 and heightMap[row + 1][col] <= heightMap[row][col]:  # down
        return False
    if col < len(heightMap[0]) - 1 and heightMap[row][col + 1] <= heightMap[row][col]:  # right
        return False
    return True


if __name__ == "__main__":
    with open('d09.in') as f:
        heightMap = [[int(i) for i in line if i != '\n'] for line in f]
    lowPoints = []
    for row in range(len(heightMap)):
        for col in range(len(heightMap[0])):
            if lowest_point(heightMap, row, col) is True:
                lowPoints.append(heightMap[row][col])
    risk_level = list(map(lambda x: x + 1, lowPoints))
    print(sum(risk_level))