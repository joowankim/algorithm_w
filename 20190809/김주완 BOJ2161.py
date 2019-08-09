'''
date: 2019-08-07
'''

from collections import deque

N = int(input())

cards = [i for i in range(1, N+1)]
deck = deque(cards)

ans = ""
while deck:
    ans += str(deck.popleft()) + ' '
    if deck:
        deck.append(deck.popleft())
print(ans)