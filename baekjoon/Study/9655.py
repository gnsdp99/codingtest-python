# 풀이 1
# print("SK" if int(input()) % 2 != 0 else "CY")

# 풀이 2. DP
import sys
input = sys.stdin.readline

N = int(input())

# 돌이 1개 또는 3개 남으면 게임이 끝남.
dp = [-1] * 1001 # 1 <= N <= 1000
# dp[k]는 돌이 k개 남았을 때 상근이 이기면 1, 창영이 이기면 0 (상근이 먼저 시작하기 때문)
dp[1] = 1
dp[2] = 0
dp[3] = 1

for i in range(4, N+1):
    if dp[i-1] or dp[i-3]: # 1개 또는 3개를 가져갔을 때 1개 또는 3개가 남으면
        dp[i] = 0 # 창영이 이김
    else:
        dp[i] = 1 # 상근이 이김
        
print("SK" if dp[N] == 1 else "CY")