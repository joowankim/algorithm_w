'''
date: 2019-07-09
'''
from queue import Queue

def index(num):
    return int(num) - 1

n = int(input())
p1, p2 = map(index, input().split())
m = int(input())
rel = [tuple(map(index, input().split())) for _ in range(m)]
adj = [[] for _ in range(n)]

for (i, j) in rel:
    adj[i] += [j]
    adj[j] += [i]

visited = [-1] * n
Q = Queue()

def bfs():
    Q.put(p1)
    visited[p1] = 0
    while Q.qsize() > 0:
        cur = Q.get()
        for nxt in adj[cur]:
            if visited[nxt] == -1:
                Q.put(nxt)
                visited[nxt] = visited[cur] + 1
                if nxt == p2:
                    print(visited[p2])
                    return
    print(-1)

bfs()