# 백준 1912 연속합 (S2)
if __name__ == "__main__":
    # 방법 1
    N = int(input().strip())
    arr = list(map(int, input().split()))
    dp = [0] * N
    dp[0] = arr[0]
    
    for i in range(1, N):
        dp[i] = max(dp[i-1] + arr[i], arr[i])
    print(max(dp))
    
    # 방법 2
    N = int(input().strip())
    arr = list(map(int, input().split()))
    
    max_sum, curr_sum = arr[0], 0
    for i in range(N):
        curr_sum = curr_sum + arr[i] if curr_sum > 0 else arr[i]
        max_sum = curr_sum if curr_sum > max_sum else max_sum
    print(max_sum)