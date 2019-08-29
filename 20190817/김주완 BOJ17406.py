'''
date: 2019-08-29
'''
from pprint import pprint
dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]    # down, up, right, left

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
turn = [tuple(map(int, input().split())) for _ in range(K)]

def permu(depth, order):
    if depth == K:
        ori = [[arr[i][j] for j in range(M)] for i in range(N)]
        for i in order:
            (r, c, s) = turn[i]
            visit = [[0] * M for _ in range(N)]
            sx, sy = r-s-1, c-s-1
            ex, ey = r+s-1, c+s-1
            cx, cy = sx, sy
            d = 2
            while not (sx, sy) == (ex, ey):
                if visit[cx][cy] and (cx, cy) == (sx, sy):
                    sx, sy = sx+1, sy+1
                    ex, ey = ex-1, ey-1
                    cx, cy = sx, sy
                    continue
                if d == 2 and cy == ey:
                    d = 0
                if d == 3 and cy == sy:
                    d = 1
                if d == 0 and cx == ex:
                    d = 3
                if d == 1 and cx == sx:
                    d = 2
                nx, ny = cx + dir[d][0], cy + dir[d][1]
                visit[nx][ny] = ori[cx][cy]
                cx, cy = nx, ny
            for i in range(N):
                for j in range(M):
                    if visit[i][j]:
                        ori[i][j] = visit[i][j]

        min_ = sum(ori[0])
        for i in range(N):
            sum_ = sum(ori[i])
            if min_ > sum_:
                min_ = sum_

        return min_

    else:
        min_ = 100000000
        for i in range(K):
            if i not in order:
                val = permu(depth+1, order+[i])
                if min_ > val:
                    min_ = val
        return min_


print(permu(0, []))
