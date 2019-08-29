'''
date: 2019-08-29
'''

N = int(input())

dp = [[0] * 10 for _ in range(N)]
dp[0] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(1, N):
    for j in range(10):
        dp[i][j] = 0
        for k in range(j, 10):
            dp[i][j] += dp[i-1][k]
print(sum(dp[N-1])%10007)