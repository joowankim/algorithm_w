'''
date: 2019-07-20
knapsack
'''

for test_case in range(1, int(input())+1):
    N, L = map(int, input().split())
    ingr = [tuple(map(int, input().split())) for _ in range(N)] # score and calorie

    dp = [[0] * (L+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, L+1):
            if ingr[i-1][1] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-ingr[i-1][1]] + ingr[i-1][0])
            else:
                dp[i][j] = dp[i-1][j]
    print("#{} {}".format(test_case, dp[N][L]))