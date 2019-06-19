for _ in range(10):
    test_case = int(input())
    nums = [list(map(int, input().split())) for _ in range(100)]
    a, b, m = 0, 0, 0
    for i in range(100):
        row = sum(nums[i])
        if row > m:
            m = row
        col = 0
        a += nums[i][i]
        b += nums[100-i-1][i]
        for j in range(100):
            col += nums[j][i]
        if col > m:
            m = col
    print('#{} {}'.format(test_case, max(a, b, m)))
