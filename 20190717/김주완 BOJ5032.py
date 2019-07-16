'''
date: 2019-07-13
'''

e, f, c = map(int, input().split())
def recur(bottle):
    if bottle < c:
        return 0
    return recur(bottle//c + bottle%c) + bottle//c
print(recur(e+f))