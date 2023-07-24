# 백준 15685 드래곤 커브 (G4)
def make_dragon_curve(d, g):
    dragon_curve = [d]
    for _ in range(g):
        for i in range(len(dragon_curve)-1, -1, -1):
            dragon_curve.append((dragon_curve[i] + 1) % 4)
    return dragon_curve

if __name__ == "__main__":
    N = int(input().strip())
    MAX_SIZE = 101
    
    # 값이 1이면 드래곤 커브의 꼭짓점
    board = [[0] * MAX_SIZE for _ in range(MAX_SIZE)]
    
    # 방향별 변화값
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    for _ in range(N):
        x, y, d, g = map(int, input().split())
        board[x][y] = 1
        dragon_curve = make_dragon_curve(d, g)
        for i in dragon_curve:
            x += dx[i]
            y += dy[i]
            board[x][y] = 1
    
    num_squre = 0
    for i in range(MAX_SIZE - 1):
        for j in range(MAX_SIZE - 1):
            if board[i][j] and board[i][j+1] and board[i+1][j] and board[i+1][j+1]:
                num_squre += 1
    print(num_squre)