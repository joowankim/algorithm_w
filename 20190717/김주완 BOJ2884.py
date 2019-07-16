'''
date: 2019-07-13
'''

H, M = map(int, input().split())

minute = H*60 + M
minute -= 45
if minute < 0:
    print(minute // 60 + 24, minute % 60)
else:
    print(minute // 60, minute % 60)