'''
date: 2019-07-03
'''

from collections import deque

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)] #north, east, south, west

def dfs(time, cur):
    global building, fires
    meet = False
    new_fires = []
    for fire in fires:
        (fx, fy) = fire
        for dir in directions:
            nx, ny = fx + dir[0], fy + dir[1]
            if 0 <= nx < h and 0 <= ny < w:
                if building[nx][ny] == '.':
                    building[nx][ny] = '*'
                    new_fires += [(nx, ny)]
                elif building[nx][ny] == '@':
                    building[nx][ny] = '*'
                    new_fires += [(nx, ny)]
                    meet = True
    fires += new_fires
    (x, y) = cur
    tmp = 10000001
    route = 4
    print(building)
    for dir in directions:
        nx, ny = x + dir[0], y + dir[1]
        if 0 <= nx < h and 0 <= ny < w:
            if building[nx][ny] == '*' or building[nx][ny] == '#':
                route -= 1
                continue
            else:
                building[nx][ny] = '@'
                building[x][y] = '.'
                t = dfs(time+1, (nx, ny))
                if tmp < t:
                    tmp = t
        else:
            return time
    if route == 0:
        return 10000000
    else:
        return tmp + 1

for test_case in range(1, int(input()) + 1):
    w, h = map(int, input().split())
    building = [list(input()) for _ in range(h)]
    fires = []
    dog = (0, 0)
    for i in range(h):
        for j in range(w):
            if building[i][j] == '*':
                fires += [(i, j)]
            elif building[i][j] == '@':
                dog = (i, j)

    result = dfs(0, dog)
    if result == 10000000:
        print('IMPOSSIBLE')
    else:
        print(result)
