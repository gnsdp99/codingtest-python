# 백준 14502 연구소 (G4)
from collections import deque
def get_combination(arr, num_to_select):
    combination = []
    if num_to_select == 0:
        return [[]]
    for i, fixed in enumerate(arr):
        rest = arr[i+1:]
        for comb in get_combination(rest, num_to_select - 1):
            combination.append([fixed] + comb)
    return combination

def spread_virus(board, walls):
    global N, M, viruses
    for i, j in walls:
        board[i][j] = 1
    
    queue = deque()
    visited = [[0] * M for _ in range(N)]
    for i, j in viruses:
        queue.append((i, j))
        while queue:
            x, y = queue.popleft()
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < N and 0 <= new_y < M and not visited[new_x][new_y]:
                    visited[new_x][new_y] = 1
                    if board[new_x][new_y] == 0:
                        board[new_x][new_y] = 2
                        queue.append((new_x, new_y))
    return board
                        
def get_num_safety(board, walls):
    global N, M
    spreaded_board = spread_virus(board, walls)
    num_safety = 0
    for i in range(N):
        for j in range(M):
            if spreaded_board[i][j] == 0:
                num_safety += 1
    return num_safety
        
if __name__== '__main__':
    N, M = map(int, input().split())
    # board = [list(map(int, input().split())) for _ in range(N)]
    blanks = []
    viruses = []
    board = []
    for i in range(N):
        line = list(map(int, input().split()))
        board.append(line)
        for j in range(len(line)):
            if line[j] == 0:
                blanks.append((i, j))
            elif line[j] == 2:
                viruses.append((i, j))
    
    max_safety = 0
    comb_of_wall = get_combination(blanks, 3)
    for walls in comb_of_wall:
        max_safety = max(max_safety, get_num_safety([line[:] for line in board], walls))
    print(max_safety)