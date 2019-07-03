'''
date : 2019-06-28
'''
from collections import deque

def bfs(circle):
    global circles, visited, N
    Q = deque([circles[circle]])
    visited[circle] = True
    while Q:
        (x, y, r) = Q.popleft()
        for i in range(N):
            (nx, ny, nr) = circles[i]
            if not visited[i] and (x-nx)**2 + (y-ny)**2 <= (r + nr)**2:
                visited[i] = True
                Q.append(circles[i])

for test_case in range(1, int(input())+1):
    N = int(input())
    circles = [tuple(map(int, input().split())) for _ in range(N)]
    visited = [False] * N

    group = 0
    for i in range(N):
        if not visited[i]:
            bfs(i)
            group += 1
    print(group)