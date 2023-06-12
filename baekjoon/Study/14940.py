import sys
from collections import deque
input = sys.stdin.readline

def bfs(start_y, start_x):
    visited = [[0] * num_col for _ in range(num_row)]
    visited[start_y][start_x] = 1
    queue = deque([(start_y, start_x, 0)]) # (y, x, cnt)
    while queue:
        curr_y, curr_x, cnt = queue.popleft()
        distances[curr_y][curr_x] = cnt
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            new_y, new_x = curr_y+dy, curr_x+dx
            if 0 <= new_y < num_row and 0 <= new_x < num_col:
                if not visited[new_y][new_x] and board[new_y][new_x] == 1:
                    queue.append((new_y, new_x, cnt+1))
                    visited[new_y][new_x] = 1
        

if __name__ == "__main__":
    num_row, num_col = map(int, input().split())
    board = []
    distances = []
    for i in range(num_row):
        board.append(list(map(int, input().split())))
        if 2 in board[i]:
            goal_y, goal_x = i, board[i].index(2)
            
        distances.append([num if num in (0, 2) else -1 for num in board[i]])

    bfs(goal_y, goal_x)
    for i in range(num_row):
        print(*distances[i])