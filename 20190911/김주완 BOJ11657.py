'''
date: 2019-09-06
'''

N, M = map(int, input().split())
adj = [tuple(map(int, input().split())) for _ in range(M)]
max_ = 999999999999
dist = [max_] * N
dist[0] = 0
cycle = False
for i in range(N+1):
    for (src, des, cost) in adj:
        if dist[src-1] != max_ and dist[des-1] > dist[src-1] + cost:
            dist[des-1] = dist[src-1] + cost
            if i == N:
                cycle = True
if cycle:
    print(-1)
else:
    for i in range(1, N):
        if dist[i] == max_:
            print(-1)
        else:
            print(dist[i])
