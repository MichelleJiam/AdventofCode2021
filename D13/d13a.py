#!/usr/bin/env python
coordinates = []
with open('test.in') as f:
    coordinates = [tuple(int(i) for i in line.split(",")) for line in f if line.strip() and "fold" not in line]
    folding = [tuple(plane, n) for  in line) for line in f if "fold" in line]
print(coordinates)