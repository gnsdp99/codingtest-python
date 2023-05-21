import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split())) # 수열

dp = [1 for _ in range(N)] # dp[i]는 0 ~ i까지의 증가 부분 수열의 길이
curr_max, max_len = A[0], dp[0]

for i in range(1, N):
    if A[i] > curr_max:
        dp[i] = max_len + 1
        curr_max = A[i]
    else:
        for j in range(i):
            if A[i] > A[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
         
    max_len = dp[i] if dp[i] > max_len else max_len    
    
print(max_len)