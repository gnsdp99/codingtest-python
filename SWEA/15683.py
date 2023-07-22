# 백준 15683 감시 (G4)
from collections import deque
def bfs(cctv_x, cctv_y, direction) -> set:
    global N, M, board
    detection_set = set()
    queue = deque([(cctv_x + dx, cctv_y + dy, dx, dy) for dx, dy in direction])
    while queue:
        x, y, dx, dy = queue.popleft()
        if 0 <= x < N and 0 <= y < M:
            if board[x][y] == 6:
                continue
            if board[x][y] == 0:
                detection_set.add((x, y))
            queue.append((x + dx, y + dy, dx, dy))
    return detection_set

def detect(cctv_x, cctv_y, cctv_num) -> list:
    detection_list = []
    directions = [
        [],
        [[(0, 1)], [(1, 0)], [(0, -1)], [(-1, 0)]],
        [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],
        [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
        [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]],
        [[(-1, 0), (0, 1), (1, 0), (0, -1)]]
    ]
    for direction in directions[cctv_num]:
        detection_list.append(bfs(cctv_x, cctv_y, direction))
    return detection_list

def dfs(curr_set, rest_arr):
    global max_num_detection
    if not rest_arr:
        max_num_detection = max(max_num_detection, len(curr_set))
        return 
    
    for fixed_set in rest_arr[0]:
        dfs(curr_set, rest_arr[1:])
       
if __name__ == "__main__":
    N, M = map(int, input().split())
    board = []
    num_blank = 0
    cctv_info = []
    for i in range(N):
        line = list(map(int, input().split()))
        board.append(line)
        for j in range(len(line)):
            if line[j] == 0:
                num_blank += 1
            if line[j] in (1, 2, 3, 4, 5):
                cctv_info.append((i, j, line[j]))
    
    detection_info = []
    for x, y, cctv_num in cctv_info:
        detection_info.append(detect(x, y, cctv_num))
    max_num_detection = 0
    dfs(set(), detection_info)
    
    print(num_blank - max_num_detection)