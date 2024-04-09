import sys

N, M = map(int, input().split())

def seq(part, seq_list):
    if len(part) == M:
        seq_list.append(part)
        # print(seq_list)
        return seq_list
    else:
        for i in range(1,N+1):
            new = part + [i]
            # print(new, '----------------')
            seq(new, seq_list)
    return seq_list

result = seq([],[])
for i in result:
    print(*i)