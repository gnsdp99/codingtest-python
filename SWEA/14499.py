# 백준 14499 주사위 굴리기 (G4)
def move_dice(x, y, command):
    global dice, N, M
    if (x <= 0 and command == 3) or (x >= N-1 and command == 4)\
        or (y <= 0 and command == 2) or (y >= M-1 and command == 1):
            return x, y
        
    if command == 1:
        y += 1
        dice = [dice[2], dice[1], 7 - dice[0]]
    elif command == 2:
        y -= 1
        dice = [7 - dice[2], dice[1], dice[0]]
    elif command == 3:
        x -= 1
        dice = [7 - dice[1], dice[0], dice[2]]
    elif command == 4:
        x += 1
        dice = [dice[1], 7 - dice[0], dice[2]]
        
    move_value(x, y, dice[0])
    print_top(7 - dice[0])
    return x, y

def move_value(x, y, under):
    global board, dice_values
    if board[x][y] == 0:
        board[x][y] = dice_values[under]
    else:
        dice_values[under] = board[x][y]
        board[x][y] = 0
    
def print_top(top):
    print(dice_values[top])

if __name__ == "__main__":
    N, M, x, y, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    commands = list(map(int, input().split()))
    dice = [1, 5, 3] # [바닥, 앞쪽, 오른쪽]
    dice_values = {k: 0 for k in range(1, 7)}
    for command in commands:
        x, y = move_dice(x, y, command)