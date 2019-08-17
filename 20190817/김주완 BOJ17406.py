'''
date: 2019-08-17
'''

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]    # down, up, right, left

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
turn = [tuple(map(int, input().split())) for _ in range(K)]

def permu(depth, order):
    if depth == K:
        ori = arr[:]
        for (r, c, s) in order:
            tmp = ori[:]
            for k in range(1, s+1):
                top_left = (r-k-1, c-k-1)
                top_right = (r-k-1, c+k-1)
                bottom_right = (r+k-1, c+k-1)
                bottom_left = (r+k-1, c-k-1)
                for i in range(top_left[0], bottom_right[0]+1):
                    for j in range(top_left[1], bottom_right[1]+1):
                        if i == top_left[0] and top_left[1] <= j < top_right[1]:
                            nx, ny = i + dir[2][0], j + dir[2][1]
                            tmp[nx][ny] = ori[i][j]
                        elif j == top_right[1] and top_right[0] <= i < bottom_right[0]:
                            nx, ny = i + dir[0][0], j + dir[0][1]
                            tmp[nx][ny] = ori[i][j]
                        elif i == bottom_right[0] and bottom_left[1] < j <= bottom_right[0]:
                            nx, ny = i + dir[3][0], j + dir[3][1]
                            tmp[nx][ny] = ori[i][j]
                        elif j == bottom_left[1] and top_left[0] < i <= bottom_left[0]:
                            nx, ny = i + dir[1][0], j + dir[1][1]
                            tmp[nx][ny] = ori[i][j]
            ori = tmp[:]
        min_ = 1000000000
        for i in range(N):
            sum_ = sum(ori[i])
            if min_ > sum_:
                min_ = sum_

        return min_

    else:
        min_ = 100000000
        for i in range(K):
            if turn[i] not in order:
                val = permu(depth+1, order+[turn[i]])
                if min_ > val:
                    min_ = val
        return min_


print(permu(0, []))
