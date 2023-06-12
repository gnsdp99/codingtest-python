"""
1 → 1 (1)
2 → 2 ~ 7 (6)
3 → 8 ~ 19 (12)
4 → 20 ~ 37 (18)
1부터 시작해서 6의 배수로 진행됨.
따라서 2부터 N까지 6의 배수씩 증가시키면서 1씩 카운트한다.
"""
import sys
input = sys.stdin.readline

N = int(input())

ans = 1 # start from 1
i, j = 2, 1 
while i <= N:
    ans += 1
    i += 6 * j
    j += 1
print(ans)