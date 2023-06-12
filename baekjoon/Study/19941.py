import sys
input = sys.stdin.readline
N, K = map(int, input().split())
PH = list(input()) # Person or Hamburger

ans = 0
for i in range(len(PH)):
    if PH[i] == 'X': # 먹은 햄버거와 먹은 사람에는 임의로 'X'를 할당한다.
        continue
    
    for j in range(i+1, min(i+K+1, len(PH))):
        if (PH[i] == 'P' and PH[j] == 'H') or (PH[i] == 'H' and PH[j] == 'P'):
            PH[i] = PH[j] = 'X'
            ans += 1
            break

print(ans)

# 피어 리뷰
# 기준을 사람으로 잡아서 그 사람 기준 왼쪽부터 오른쪽까지 탐색함.
import sys
input = sys.stdin.readline
n, k = map(int, input().split())
burger = list(input().rstrip())
result = 0
for i, ham in enumerate(burger):
    if ham == 'P':
        for j in range(max(i-k, 0), min(n, i+k+1)):
            if burger[j] == 'H':
                burger[j] = 'E'
                result += 1
                break
print(result)
