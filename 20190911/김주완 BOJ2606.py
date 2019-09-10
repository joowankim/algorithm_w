'''
date: 2019-09-06
'''

from collections import deque

n = int(input())
adj_num = int(input())
adj = [tuple(map(int, input().split())) for _ in range(adj_num)]
conn = [[] for _ in range(n)]

for (i, j) in adj:
    conn[i-1] += [j-1]
    conn[j-1] += [i-1]

def bfs():
    Q = deque([0])
    visited = [0] * n
    visited[0] = 1
    while Q:
        node = Q.popleft()
        for i in conn[node]:
            if not visited[i]:
                Q.append(i)
                visited[i] = 1
    return sum(visited) - 1

print(bfs())