import sys

N = int(input())

line = list(map(int, input().split()))

stack = list()
snack = 'Nice'
pos = 1

while(len(line) != 0):
    if len(stack) != 0:
        if stack[-1] == pos:
            stack.pop(-1)
            pos += 1
            continue
    first = line.pop(0)
    if first == pos:
        pos += 1
        continue
    elif first != pos:
        if len(stack) != 0:
            if stack[-1] != pos:
                stack.append(first)
        elif len(stack) == 0:
            stack.append(first)

for i in stack:
    if stack[-1] == pos:
        pos += 1
        stack.pop(-1)
        continue
    else:
        snack = 'Sad'
print(snack)