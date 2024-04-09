import sys

N = int(input())
dance = {'ChongChong': 1}

for _ in range(N):
    ai, bi = input().split()
    if ai in dance.keys() or bi in dance.keys():
        if ai not in dance.keys():
            dance[ai] = 1
        if bi not in dance.keys():
            dance[bi] = 1

print(len(dance.keys()))