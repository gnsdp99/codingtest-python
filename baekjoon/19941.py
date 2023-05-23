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