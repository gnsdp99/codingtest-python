# 백준 2839 설탕배달 (S4)
if __name__ == "__main__":
    N = int(input().strip())
    MAX_SIZE = 5001
    dp = [float('inf')] * MAX_SIZE
    dp[3], dp[5] = 1, 1
    
    for i in range(6, N+1):
        dp[i] = min(dp[i-3] + 1, dp[i-5] + 1, dp[i-3] + dp[i-5] + 1)
    
    print(dp[N]) if dp[N] != float('inf') else print(-1)