# 백준 3190 뱀 (G4)
from collections import deque
def move_to_next(direction):
    global board, snakes
    head_x, head_y = snakes[-1]
    if direction == 0:
        head_x = head_x - 1
    elif direction == 1:
        head_y = head_y + 1
    elif direction == 2:
        head_x = head_x + 1
    elif direction == 3:
        head_y = head_y - 1
        
    if board[head_x][head_y] in (1, 3):
        return 0
    if board[head_x][head_y] == 0:
        tail_x, tail_y = snakes.popleft()
        board[tail_x][tail_y] = 0
    snakes.append((head_x, head_y))
    board[head_x][head_y] = 3
    return 1
        
def rotate(curr, rotating):
    if rotating == 'D': # right
        # 0 -> 1 -> 2 -> 3 -> 0
        return (curr + 1) % 4
    elif rotating == 'L': # left
        # 0 -> 3 -> 2 -> 1 -> 0
        return (curr + 3) % 4

if __name__ == "__main__":
    N, K = int(input().rstrip()), int(input().rstrip())
    board = [[1] * (N+2)] + [[1] + [0] * (N) + [1] for _ in range(N)] + [[1] * (N+2)] # 0: 빈 칸, 1: 벽, 2: 사과, 3: 뱀
    board[1][1] = 3
    snakes = deque([(1, 1)])
    
    for _ in range(K):
        row, col = map(int, input().split())
        board[row][col] = 2

    L = int(input().rstrip())
    rotation = deque()
    for _ in range(L):
        X, C = input().split()
        rotation.append((int(X), C))
        
    curr_direction = 1 # N: 0, 1: E, 2: S, 3: W
    curr_time = 0
    is_playing = 1
    while is_playing:
        is_playing = move_to_next(curr_direction)
        curr_time += 1
        if rotation and rotation[0][0] == curr_time:
            curr_direction = rotate(curr_direction, rotation[0][1])
            rotation.popleft()
    
    print(curr_time)