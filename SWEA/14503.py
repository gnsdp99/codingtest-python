# 14503 로봇 청소기 G5
def clean(i, j, num_cleaning):
    if board[i][j] == 0:
        board[i][j] = 2
        return num_cleaning + 1
    else:
        return num_cleaning

def search_counter_clockwise(i, j, d):
    new_i, new_j, new_d = move_forward(i, j, d)
    if new_i != i or new_j != j:
        return new_i, new_j, new_d

    new_i, new_j = move_backward(i, j, d)
    return new_i, new_j, d

def move_forward(i, j, d):
    for _ in range(4):
        d = (d + 3) % 4
        
        if d == 0 and board[i-1][j] == 0:
            return i-1, j, d
        elif d == 1 and board[i][j+1] == 0:
            return i, j+1, d
        elif d == 2 and board[i+1][j] == 0:
            return i+1, j, d
        elif d == 3 and board[i][j-1] == 0:
            return i, j-1, d
    return i, j, d

def move_backward(i, j, d):
    if d == 0 and board[i+1][j] == 2:
        return i+1, j
    elif d == 1 and board[i][j-1] == 2:
        return i, j-1
    elif d == 2 and board[i-1][j] == 2:
        return i-1, j
    elif d == 3 and board[i][j+1] == 2:
        return i, j+1
    else: # 벽
        return -1, -1
    
if __name__ == "__main__":
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    # 반시계 방향 0 -> 3 -> 2 -> 1 -> 0
    board = [list(map(int, input().split())) for _ in range(N)]

    num_cleaning = 0 # 최종 답
    
    while r != -1 and c != -1:
        num_cleaning = clean(r, c, num_cleaning)
        r, c, d = search_counter_clockwise(r, c, d)
        
    print(num_cleaning)