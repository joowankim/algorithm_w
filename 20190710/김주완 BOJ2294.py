'''
date: 2019-07-09
'''
n, k = map(int, input().split())
v = [int(input()) for _ in range(n)]

def coin():
    dp = [0] * (k+1)
    for i in range(1, k+1):
        min_coins = 10001
        for j in range(n):
            if v[j] <= i and min_coins > dp[i-v[j]] + 1:
                min_coins = dp[i-v[j]] + 1
        dp[i] = min_coins
    return dp[k]
r = coin()
if r == 10001:
    print(-1)
else:
    print(r)