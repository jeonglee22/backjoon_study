import sys
from collections import deque

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

M = int(input())
C = list(map(int, input().split()))
result = list()

queue_list = deque()
for i in range(M):
    queue_list.appendleft(C[i])

for i in range(N):
    if A[i] == 0:
        queue_list.append(B[i])

for i in range(M):
    result.append(queue_list.pop())

print(*result)