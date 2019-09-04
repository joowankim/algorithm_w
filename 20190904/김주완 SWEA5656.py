'''
date: 2019-09-04
'''
from pprint import pprint
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def boom(map_ , x, y, visit):
    global W, H
    visit += [(x, y)]
    range_ = map_[x][y]
    map_[x][y] = 0
    for dir in directions:
        for i in range(1, range_):
            nx, ny = x + dir[0]*i, y + dir[1]*i
            if 0 <= nx < H and 0 <= ny < W:
                if map_[nx][ny] != 0 and (nx, ny) not in visit:
                    boom(map_, nx, ny, visit)
                map_[nx][ny] = 0

def rebuild(map_):
    global W, H
    for j in range(W):
        que = [0] * H
        for i in range(H):
            if map_[i][j] != 0:
                que.remove(0)
                que += [map_[i][j]]
        for i in range(H):
            map_[i][j] = que[i]

def drop(map_, pos):
    global W, H
    change = False
    for i in range(H):
        if map_[i][pos] != 0:
            boom(map_, i, pos, [])
            change = True
            break
    if change:
        rebuild(map_)

def dfs(depth, order):
    global MAP, N, W, H
    if depth == N:
        map_ = [[MAP[i][j] for j in range(W)] for i in range(H)]
        for i in order:
            drop(map_, i)
        cnt = 0
        for i in range(H):
            for j in range(W):
                if map_[i][j] != 0:
                    cnt += 1
        return cnt
    else:
        min_ = W * H
        for i in range(W):
            r = dfs(depth+1, order+[i])
            if min_ > r:
                min_ = r
        return min_

for test_case in range(1, int(input())+1):
    N, W, H = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(H)]

    print("#{} {}".format(test_case, dfs(0, [])))

