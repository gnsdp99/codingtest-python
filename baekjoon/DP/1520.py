import sys
input = sys.stdin.readline
M, N = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(M)]
# dp[i][j]는 heights[i][j]에서 도착 지점까지 갈 수 있는 길의 개수를 의미한다.
dp = [[-1] * N for _ in range(M)]
dp[-1][-1] = 1 # 도착 지점은 무조건 1

def dfs(y, x):
    # 방문한 곳은 dp값 리턴
    if dp[y][x] != -1: return dp[y][x]
    dp[y][x] = 0 # 방문 표시
    
    for (dy, dx) in ((-1, 0), (1, 0), (0, -1), (0, 1)): # 상하좌우 탐색
        new_y, new_x = y + dy, x + dx
        if not (0 <= new_y < M) or not (0 <= new_x < N): # 범위 제한
            continue
        
        # 더 낮은 곳만 탐색
        if heights[y][x] > heights[new_y][new_x]:
            dp[y][x] += dfs(new_y, new_x)
    
    return dp[y][x]

if __name__ == '__main__':
    dfs(0, 0) # 시작 지점부터 탐색
    print(dp[0][0])