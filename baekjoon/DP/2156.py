import sys
input = sys.stdin.readline
N = int(input())
wine = [0] + [int(input()) for _ in range(N)]
dp = [wine[0], wine[1]]

if N > 1:
    dp.append(wine[1] + wine[2])

for i in range(3, N+1):
    # dp[i-1] >> 현재 값을 저장하지 않은 최댓값.
    # dp[i-2] + wine[i] >> 이전 값을 더하지 않은 최댓값에 현재 값을 더함.
    # dp[i-3] + wine[i-1] + wine[i] >> 이전값과 전전값을 더하지 않은 최댓값에 이전 값과 현재 값을 더함
    dp.append(max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i]))

print(dp[-1])