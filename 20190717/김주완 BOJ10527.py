'''
date:2019-07-13
'''
import sys

n = int(input())
DOM = {}
Kat = {}

for _ in range(n):
    line = sys.stdin.readline()
    if line in DOM.keys():
        DOM[line] += 1
    else:
        DOM[line] = 1

for _ in range(n):
    line = sys.stdin.readline()
    if line in Kat.keys():
        Kat[line] += 1
    else:
        Kat[line] = 1
cnt = 0
for key in DOM.keys():
    if key in Kat.keys():
        cnt += DOM[key] if DOM[key] < Kat[key] else Kat[key]
print(cnt)