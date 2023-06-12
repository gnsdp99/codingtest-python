import sys
input = sys.stdin.readline

N, K = map(int, input().split())

medals = [[] for _ in range(N)] # 각 국가의 메달 개수
for _ in range(N):
    i, *rest = map(int, input().split())
    medals[i-1] = rest

# K번째 국가의 메달 개수
k_medal = medals[K-1] # 인덱스는 0부터

# 정렬
medals = sorted(medals, key=lambda x:(x[0], x[1], x[2]), reverse=True)

# K번째 국가의 등수
ans = medals.index(k_medal) + 1 # 등수는 1등부터
print(ans)