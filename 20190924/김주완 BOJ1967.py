from collections import deque
import sys

n = int(sys.stdin.readline())
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n-1)]
adj = [[] for _ in range(n)]

for (i, j, c) in edges:
    adj[i-1] += [(j-1, c)]
    adj[j-1] += [(i-1, c)]

leaves = []
for i in range(n):
    if len(adj[i]) == 1:
        leaves += [i]

def dia(src, v):
    Q = deque([src])
    visited = [0] * n
    for i in v:
        visited[i] = -1
    while Q:
        root = Q.popleft()
        for (nxt, cost) in adj[root]:
            if not visited[nxt]:
                Q.append(nxt)
                visited[nxt] = visited[root] + cost
    return max(visited)

max_ = 0
visit = []
for i in leaves:
    max_ = max(max_, dia(i, visit))
    visit += [i]
print(max_)