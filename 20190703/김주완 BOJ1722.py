'''
date : 2019-06-29
'''
# N = int(input())
# line = input()
# problem, k = line[0], line[2:] + ' '
# order = 0
# visit = [False] * N
#
# def dfs(depth, seq):
#     global order
#     # print(depth, [seq])
#     if depth == N:
#         order += 1
#         if problem == '1':
#             if int(k) == order:
#                 print(seq)
#                 return True
#             return False
#         else:
#             if k == seq:
#                 print(order)
#                 return True
#             return False
#     else:
#         for i in range(1, N+1):
#             if visit[i-1]:
#                 continue
#             else:
#                 visit[i-1] = True
#                 if dfs(depth+1, seq + str(i) + ' '):
#                     return True
#                 visit[i-1] = False
# from time import time
# s = time()
# dfs(0, '')
# print('{} seconds'.format(time() - s))

N = int(input())
line = list(map(int, input().split()))
problem, k = line[0], line[1:]

fac = [1]
for i in range(1, N+1):
    fac += [fac[i-1] * i]
check = [False] * N

if problem == 1:
    seq = ''
    for i in range(N):
        for j in range(1, N+1):
            if check[j-1]:
                continue
            if k[0] > fac[N-i-1]:
                k[0] -= fac[N-i-1]
            else:
                seq += str(j) + ' '
                check[j-1] = True
                break
    print(seq)
else:
    order = 0
    for i in range(N):
        for j in range(k[i]-1):
            if not check[j]:
                order += fac[N-i-1]
        check[k[i]-1] = True
    print(int(order)+1)