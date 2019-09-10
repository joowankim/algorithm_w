'''
date: 2019-09-06
'''
from collections import deque

go = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

def bfs(src, des, n):
    Q = deque([src])
    visited = [[-1] * n for _ in range(n)]
    visited[src[0]][src[1]] = 0
    while Q:
        (x, y) = Q.popleft()
        for (dx, dy) in go:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == -1:
                    Q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    if (nx, ny) == des:
                        break
    return visited[des[0]][des[1]]

for test_case in range(1, int(input()) + 1):
    n = int(input())
    src = tuple(map(int, input().split()))
    des = tuple(map(int, input().split()))

    print(bfs(src, des, n))
