# 백준 10844 쉬운 계단 수 (S1)
if __name__ == "__main__":
    N = int(input().strip())
    dp = [[0] * 10 for _ in range(N+1)]
    dp[1] = [0] + [1] * 9
    
    for i in range(2, N+1):
        dp[i][0] = dp[i-1][1]
        for j in range(1, 9):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        dp[i][9] = dp[i-1][8]
    
    ans = sum(dp[N]) % 1_000_000_000
    print(ans) 