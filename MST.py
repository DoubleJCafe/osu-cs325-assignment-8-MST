# Name: Joshua Jansen
# OSU Email: Jansejos@oregonstate.edu
# Course: CS325
# Assignment: 8

import heapq


def Prims(G):
    s = 0

    dist = [float('inf')] * len(G)
    prev = [None] * len(G)
    dist[s] = 0

    heap = [(0, s)]
    visited = []
    MST = []

    while len(visited) < len(G):
        min_dist, vertex = heapq.heappop(heap)
        if vertex not in visited:
            visited.append(vertex)
            if prev[vertex] is not None:
                MST.append((prev[vertex], vertex, G[prev[vertex]][vertex]))

            for node in range(len(G)):
                if G[vertex][node] != 0 and node not in visited and G[vertex][node] < dist[node]:
                    dist[node] = G[vertex][node]
                    prev[node] = vertex
                    heapq.heappush(heap, (int(dist[node]), node))

    return MST
