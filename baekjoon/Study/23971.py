# 풀이 1.
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

# 풀이 2.
# import sys
# input = sys.stdin.readline
# h, w, n, m = map(int, input().split())

# col = (h-1) // (n+1) + 1
# row = (w-1) // (m+1) + 1

# print(row*col)
