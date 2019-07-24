'''
date: 2019-07-20
'''
from collections import deque

directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]	#right, left, up, down
[right, left, up, down] = directions

for test_case in range(1, int(input()) + 1):
    R, C = map(int, input().split())
    cmd = [input() for _ in range(R)]
    visited = [[[[False] * 16 for _ in range(4)] for _ in range(C) ] for _ in range(R)]

    Q = deque()
    Q.append((0, 0, 0))
    mem = 0
    ans = False
    visited[0][0][0][mem] = True
    while Q:
        x, y, dir = Q.popleft()
        check = False
        if '0' <= cmd[x][y] <= '9':
            mem = int(cmd[x][y])
        elif cmd[x][y] == '+':
            mem = (mem + 1) % 16
        elif cmd[x][y] == '-':
            mem = (mem - 1) % 16
        elif cmd[x][y] == '<':
            dir = 1
        elif cmd[x][y] == '>':
            dir = 0
        elif cmd[x][y] == '^':
            dir = 2
        elif cmd[x][y] == 'v':
            dir = 3
        elif cmd[x][y] == '_':
            if mem == 0:
                dir = 0
            else:
                dir = 1
        elif cmd[x][y] == '|':
            if mem == 0:
                dir = 3
            else:
                dir = 2
        elif cmd[x][y] == '?':
            check = True
        elif cmd[x][y] == '@':
            ans = True
            break

        if check:
            for i in range(4):
                nx, ny = (x + directions[i][0]) % R, (y + directions[i][1]) % C
                if not visited[nx][ny][i][mem]:
                    visited[nx][ny][i][mem] = True
                    Q.append((nx, ny, i))
        else:
            nx, ny = (x + directions[dir][0]) % R, (y + directions[dir][1]) % C
            if not visited[nx][ny][dir][mem]:
                visited[nx][ny][dir][mem] = True
                Q.append((nx, ny, dir))
    if ans:
        print('#{} YES'.format(test_case))
    else:
        print('#{} NO'.format(test_case))