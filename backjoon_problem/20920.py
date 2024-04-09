import sys

N, M = map(int, input().split())

dic = {}

for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) < M:
        continue
    else :
        if word in dic.keys():
            dic[word] += 1
        else :
            dic[word] = 1

all_items = dic.items()
result = sorted(all_items, key = lambda x: (-x[1], -len(x[0]), x[0]))
for i in result:
    print(i[0])