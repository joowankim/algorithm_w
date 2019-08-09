'''
date: 2019-08-07
'''

N = int(input())

from collections import deque

cards = [i for i in range(1, N+1)]
deck = deque(cards)

ans = -1
while deck:
    ans = deck.popleft()
    if deck:
        deck.append(deck.popleft())
print(ans)