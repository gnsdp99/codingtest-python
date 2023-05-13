# 풀이 1
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
# 구간 합
sums = 0
remainder = [0 for _ in range(M)] # 나머지는 0 ~ M-1까지
for i in range(len(num)):
    sums += num[i]
    remainder[sums % M] += 1

res = remainder[0] # 나머지가 0인 구간 합

# 나머지가 동일한 구간 합 p와 q에서 (q - p)는 나머지가 0이다.
for k in remainder:
    res += k * (k-1) // 2 # k개 중 2개 조합

print(res)