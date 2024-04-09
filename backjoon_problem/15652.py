import sys

N, M = map(int, input().split())

def seq(part, seq_list):
    if len(part) == M:
        seq_list.append(part)
        # print(seq_list)
        return seq_list
    else:
        for i in range(1,N+1):
            if len(part) != 0 and part[-1] > i:
                continue
            else:
                new = part + [i]
                seq(new, seq_list)
    return seq_list

result = seq([],[])
for i in result:
    print(*i)