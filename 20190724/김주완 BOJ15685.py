'''
date: 2019-07-19
'''

dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]

N = int(input())
inf = [list(map(int, input().split())) for _ in range(N)]

def turn(p):
    (y, x) = p
    nx = x*0 + y*(-1)
    ny = x*1 + y*0
    return (ny, nx)

def trans(p, s):
    (sy, sx) = s
    (y, x) = p
    return (y - sy, x - sx)

def curve(start, d, cur, gen, points):
    if cur > gen:
        return points
    else:
        if cur == 0:
            s = (start[0] + dirs[d][0], start[1] + dirs[d][1])
            points += [s]
            return curve(points[-1], d, cur+1, gen, points)
        else:
            for i in range(len(points)-2, -1, -1):
                p = trans(points[i], start)
                p = turn(p)
                p = trans(p, (start[0]*(-1), start[1]*(-1)))
                if 0 <= p[0] <= 100 and 0 <= p[1] <= 100:
                    points += [p]
            return curve(points[-1], d, cur+1, gen, points)
p = []
cor = [[0]*101 for _ in range(101)]
for info in inf:
    [x, y, d, g] = info
    p += curve((y, x), d, -1, g, [(y, x)])
    for po in p:
        cor[po[0]][po[1]] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if cor[i][j] == 1:
            if cor[i][j+1] == 1 and cor[i+1][j] ==1 and cor[i+1][j+1]:
                cnt += 1

print(cnt)
