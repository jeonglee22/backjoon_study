import sys
from collections import deque

deck = deque()

N = int(input())

for _ in range(N):
    command = sys.stdin.readline().split()
    
    if command[0] == '1':
        deck.appendleft(int(command[1]))
    elif command[0] == '2':
        deck.append(int(command[1]))
    elif command[0] == '3':
        if len(deck) == 0:
            print(-1)
        else :
            front = deck.popleft()
            print(front)
    elif command[0] == '4':
        if len(deck) == 0:
            print(-1)
        else :
            back = deck.pop()
            print(back)
    elif command[0] == '5':
        print(len(deck))
    elif command[0] == '6':
        if len(deck) == 0:
            print(1)
        else :
            print(0)
    elif command[0] == '7':
        if len(deck) == 0:
            print(-1)
        else :
            front = deck[0]
            print(front)
    elif command[0] == '8':
        if len(deck) == 0:
            print(-1)
        else :
            back = deck[-1]
            print(back)