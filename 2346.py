import sys
from collections import deque

N = int(input())

move_list = deque(list(map(int, input().split())))

num_list = deque([i+1 for i in range(N)])
result_list = list()

while(len(num_list) != 0):
    current_num = num_list.popleft()
    result_list.append(current_num)
    if len(num_list) == 0:
        break
    move = move_list[current_num-1]
    if move > 0:
        for i in range(move-1):
            first = num_list.popleft()
            num_list.append(first)
    elif move < 0:
        for i in range(move*(-1)):
            end = num_list.pop()
            num_list.appendleft(end)

print(*result_list)