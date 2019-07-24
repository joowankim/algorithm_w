'''
date: 2019-07-19
'''

op = ['+', '-', '*', '/']

N = int(input())
nums = list(map(int, input().split()))
operations = list(map(int, input().split()))    # +, -, *, /

def dfs(oper, order):
    if len(order) == N-1:
        s = nums[0]
        for i in range(N-1):
            if order[i] == '+':
                s += nums[i+1]
            elif order[i] == '-':
                s -= nums[i+1]
            elif order[i] == '*':
                s *= nums[i+1]
            elif order[i] == '/':
                s = int(s/nums[i+1])
        return [s, s]
    else:
        min_res = 1000000001
        max_res = -1000000001
        for i in range(4):
            if oper[i] > 0:
                oper[i] -= 1
                res = dfs(oper, order + [op[i]])
                if res[1] < min_res:
                    min_res = res[1]
                if res[0] > max_res:
                    max_res = res[0]
                oper[i] += 1
        return [max_res, min_res]
result = dfs(operations, [])
print(result[0])
print(result[1])