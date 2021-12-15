#!/usr/bin/env python3

import heapq as hq
import math


# def dijkstra(risk_map, start):
#     length = len(risk_map)
#     visited = [False] * length
#     risk = [math.inf] * length
#     path = [None] * length
#     unvisited = []
#     risk[start] = 0
#     hq.heappush(unvisited, (0, start))
#     while len(unvisited) > 0:
#         n_risk, n_index = hq.heappop(unvisited)
#         visited[n_index] = True
#         for cur_node, w in enumerate(risk_map[n_index]):
#             if not visited[cur_node]:
#                 cur_risk = n_risk + w
#                 if cur_risk < risk[cur_node]:
#                     risk[cur_node] = cur_risk
#                     path[cur_node] = n_index
#                     hq.heappush(unvisited, (cur_risk, cur_node))
#     return path, risk

#
def heuristic(a: node_location, b: node_location) -> float:
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

def a_star_search(risk_map, start, goal):
    frontier = []
    hq.heappush(frontier, (start, 0))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while len(frontier) > 0:
        cur_node, cur_risk = hq.heappop(frontier)
        if cur_node == goal:
            break

        for node in risk_map[cur_node[0]][cur]:




with open('test.in') as f:
    risk_map = [[int(i) for i in line if i != '\n'] for line in f]
cost = [ [ 1, 2, 3 ], [ 4, 8, 2 ], [ 1, 5, 3 ] ]
# print(dijkstra(risk_map, 0))