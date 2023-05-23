import sys
input = sys.stdin.readline
N = int(input())

dp = [[1] * 10 for _ in range(N)]
# 점화식
# dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
# dp[i][9] = dp[i-1][8] / dp[i][0] = dp[i-1][1]
for i in range(1, N):
    dp[i][0] = dp[i-1][1]
    for j in range(1, 9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    dp[i][9] = dp[i-1][8]
    
# 0으로 시작하는 경우는 제외해야 함.
ans = sum(dp[N-1][1:]) % 1_000_000_000
print(ans)