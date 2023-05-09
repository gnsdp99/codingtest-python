import sys
input = sys.stdin.readline

N = int(input())
info = [tuple(map(int, input().split())) for _ in range(N)] # (weight, height)

res = [1 for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        
        # count the number of bigger one
        if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            res[i] += 1
            
for i in range(N):
    print(res[i], end=' ')