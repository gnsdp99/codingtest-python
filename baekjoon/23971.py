import sys
input = sys.stdin.readline

H, W, N, M = map(int, input().split())

r = c = 0 # the num of row, column

for _ in range(0, W, M+1):
    c += 1
    
for _ in range(0, H, N+1):
    r += 1    
    
ans = r * c
print(ans)