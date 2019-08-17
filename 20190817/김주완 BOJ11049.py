'''
date: 2019-08-16
'''

N = int(input())
mat = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[-1] * N for _ in range(N)]
def sol(x, y):
    if x == y:
        return 0
    if dp[x][y] is not -1:
        return dp[x][y]

    min_ = 2**31
    for i in range(x, y):
        min_ = min(min_, sol(x, i) + sol(i+1, y) + mat[x][0]*mat[i][1]*mat[y][1])
    return min_

print(sol(0, N-1))