import sys
input = sys.stdin.readline

def dfs(y, x, curr_sum, cnt):
    # T모양을 제외한 나머지 테트로미노
    global max_sum
    if cnt == 4:
        max_sum = max(max_sum, curr_sum)
        return
    
    for dy, dx in delta:
        new_y, new_x = y + dy, x + dx
        if 0 <= new_y < N and 0 <= new_x < M:
            if not visited[new_y][new_x]:
                visited[new_y][new_x] = 1
                dfs(new_y, new_x, curr_sum + board[new_y][new_x], cnt+1)
                visited[new_y][new_x] = 0

def tetromino_T(y, x):
    global max_sum
    for i in range(4):
        curr_sum = board[y][x]
        for j in range(3):
            # delta의 방향이 [상, 하, 좌, 우]이다.
            # 가능한 방향 조합은 (상하좌=012, 하좌우=123, 좌우상=230, 우상하=301)다.
            k = (i + j) % 4
            new_y, new_x = y + delta[k][0], x + delta[k][1]
            if 0 <= new_y < N and 0 <= new_x < M:
                curr_sum += board[new_y][new_x]
            else:
                curr_sum = 0
                break

        max_sum = max(max_sum, curr_sum)

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    max_sum = 0
    for y in range(N):
        for x in range(M):
            visited[y][x] = 1
            dfs(y, x, board[y][x], 1)
            visited[y][x] = 0
            
            tetromino_T(y, x)
            
    print(max_sum)