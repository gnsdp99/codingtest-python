# 백준 17144 미세먼지 안녕 (G4)
def spread_dust():
    # origin board를 기준으로 확산된 미세먼지를 new board에 기록
    new_board = [[0] * C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if board[y][x] == -1:
                new_board[y][x] = -1
            if board[y][x] > 0:
                amount_spread = board[y][x] // 5
                count_spread = 0
                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if 0 <= ny < R and 0 <= nx < C and board[ny][nx] != -1:
                        new_board[ny][nx] += amount_spread
                        count_spread += 1
                new_board[y][x] += (board[y][x] - amount_spread * count_spread)
    
    return new_board

def purify(top_air = True):
    # top: 우 -> 상 -> 좌 -> 하 (1, 0, 3, 2)
    # bot: 우 -> 하 -> 좌 -> 상 (1, 2, 3, 0)
    cy = top if top_air else bot
    cx = 1
    direct = 1
    prev = 0
    while True:
        if cy in (top, bot) and cx == 0:
            break
        ny, nx = cy + dy[direct], cx + dx[direct]
        if ny < 0 or ny >= R or nx < 0 or nx >= C:
            direct = (direct + 3) % 4 if top_air else (direct + 1) % 4
            continue
        
        board[cy][cx], prev = prev, board[cy][cx]
        cy, cx = ny, nx
        
if __name__ == "__main__":
    R, C, T = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(R)]
    # 12시 기준 시계방향 (상, 우, 하, 좌)
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    # 공기청정기 위치 찾기
    top, bot = -1, -1
    for i in range(R):
        if board[i][0] == -1:
            top, bot = i, i+1
            break
        
    for _ in range(T):
        board = spread_dust()
        purify(top_air=True)
        purify(top_air=False)

    # 미세먼지 양 출력
    amount_dust = 0
    for i in range(R):
        amount_dust += sum([num for num in board[i] if num != -1])
    print(amount_dust)