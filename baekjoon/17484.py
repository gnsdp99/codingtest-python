# 풀이 1. 완전탐색 (재귀 호출)
import sys

def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    direction = (-1, 0, 1)
    def brute_force(y, x, prev):
        if y == N:
            return 0
        fuel = float("inf")
        for i in range(3):
            if direction[i] == prev: # 이전 방향과 동일
                continue
            next_x = x + direction[i]
            if (next_x < 0) or (next_x >= M): # 범위 초과
                continue
            fuel = min(fuel, matrix[y][x] + brute_force(y+1, next_x, direction[i]))
        return fuel
                
    ans = float("inf")
    for x in range(M):
        ans = min(ans, brute_force(0, x, -2)) 
    print(ans)
    
main()

# 풀이 2. DP
import sys

MAX_VAL = 100 * 6 # 연료의 최댓값
def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    dp = [[[MAX_VAL] * 3 for _ in range(M)] for _ in range(N)] # 3차원 배열
    
    for y in range(N):
        # dp[0][i]은 matrix[0][i] 3개로 채움.
        if y == 0:
            for x in range(M):
                dp[0][x] = [matrix[0][x]] * 3
        else:
            for x in range(M):
                # dp[y][x][0]은 dp[y][x+1]에서 내려온 값이다.
                # dp[y][x][1]은 dp[y][x]에서 내려온 값이다.
                # dp[y][x][2]은 dp[y][x-1]에서 내려온 값이다.
                if x == 0:
                    dp[y][x][0] = min(dp[y-1][x+1][1], dp[y-1][x+1][2]) + matrix[y][x]
                    dp[y][x][1] = dp[y-1][x][0] + matrix[y][x]
                elif x == M-1:
                    dp[y][x][1] = dp[y-1][x][2] + matrix[y][x]
                    dp[y][x][2] = min(dp[y-1][x-1][0], dp[y-1][x-1][1]) + matrix[y][x]
                else:
                    dp[y][x][0] = min(dp[y-1][x+1][1], dp[y-1][x+1][2]) + matrix[y][x]
                    dp[y][x][1] = min(dp[y-1][x][0], dp[y-1][x][2]) + matrix[y][x]
                    dp[y][x][2] = min(dp[y-1][x-1][0], dp[y-1][x-1][1]) + matrix[y][x]
        
    ans = float("inf")
    for x in range(M):
        ans = min(ans, min(dp[-1][x]))
    print(ans)

main()