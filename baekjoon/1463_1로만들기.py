# 백준 1463 1로 만들기 (S3)
if __name__ == "__main__":
    N = int(input().strip())
    dp = [0] * 2 + [1] * (N-1)
    for i in range(4, N+1):
        dp[i] = dp[i-1] + 1
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
    
    print(dp[N])