'''
date : 2019-06-20
'''
x, y = map(int, input().split())
d = 0
for i in range(1, x):
    if i == 2:
        d += 28
    elif i in [4, 6, 9, 11]:
        d += 30
    else:
        d += 31
d += y - 1
day_of_week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
print(day_of_week[d%7])