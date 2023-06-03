import sys
import copy
from collections import deque
input = sys.stdin.readline

def find_num_safe(board_copy):
    queue = deque([(y, x) for y in range(N) for x in range(M) if board_copy[y][x] == 2])
    while queue:
        y, x = queue.popleft()
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_y, new_x = y + dy, x + dx
            if 0 <= new_y < N and 0 <= new_x < M:
                if board_copy[new_y][new_x] == 0:
                    board_copy[new_y][new_x] = 2
                    queue.append((new_y, new_x))
    
    num_safe = len([(y, x) for y in range(N) for x in range(M) if board_copy[y][x] == 0])
    return num_safe

def build_wall(num_wall):
    if num_wall == 0:
        return find_num_safe(copy.deepcopy(board))
    
    num_safe = 0
    for y in range(N):
        for x in range(M):
            if board[y][x] == 0:
                board[y][x] = 1
                num_safe = max(num_safe, build_wall(num_wall-1))
                board[y][x] = 0

    return num_safe

if __name__ == "__main__":       
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print(build_wall(3))