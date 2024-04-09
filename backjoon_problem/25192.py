import sys

N = int(input())
nick = {}
count = 0

for i in range(N):
    chat = sys.stdin.readline()[:-1]
    if chat == 'ENTER':
        nick = {}
    else :
        if chat not in nick.keys():
            nick[chat] = 1
            count += 1
        else :
            continue
print(count)