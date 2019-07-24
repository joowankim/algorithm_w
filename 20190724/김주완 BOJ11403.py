'''
date: 2019-07-20
'''

N = int(input())
adj = [list(map(int, input().split())) for _ in range(N)]

from queue import Queue

def bfs(v):
    Q = Queue()
    Q.put(v)
    visit = [0] * N
    while not Q.empty():
        cur = Q.get()
        for to in range(N):
            if visit[to] != 1 and adj[cur][to] == 1:
                Q.put(to)
                visit[to] = 1
    out = ""
    for i in range(N):
        out += str(visit[i]) + " "
    return out

for i in range(N):
    print(bfs(i))
