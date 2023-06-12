import sys
input = sys.stdin.readline
N = int(input()) # num of cities
dists = list(map(int, input().split()))
prices = list(map(int, input().split()))

ans = 0
min_price = 1_000_000_000
for i in range(N-1):
    if min_price > prices[i]:
        min_price = prices[i]
    ans += min_price * dists[i]

print(ans)