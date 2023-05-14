import sys
input = sys.stdin.readline
N = int(input())

ans = 1 if N != 1 else 0

left, right = 0, 0
end = N // 2 if N % 2 == 0 else N // 2 + 1
curr_sum = 0
while right <= end:
    if curr_sum == N:
        ans += 1
    if curr_sum <= N:
        right += 1
        curr_sum += right
    else:
        curr_sum -= left
        left += 1

print(ans)