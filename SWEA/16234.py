# 16234 인구 이동 (G5)
from collections import deque
def find_union(x, y):
    queue = deque([(x, y)])
    union = set([(x, y)])
    population = A[x][y]
    while queue:
        curr_x, curr_y = queue.popleft()
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            new_x, new_y = curr_x + dx, curr_y + dy
            if 0 <= new_x < N and 0 <= new_y < N and visited[new_x][new_y] != day:
                if L <= abs(A[curr_x][curr_y] - A[new_x][new_y]) <= R:
                    visited[new_x][new_y] = day
                    queue.append((new_x, new_y))
                    union.add((new_x, new_y))
                    population += A[new_x][new_y]
    if len(union) > 1:
        divide_population_for_union(union, population)

def divide_population_for_union(union, population):
    divided = population // len(union)
    for i, j in union:
        A[i][j] = divided
        candidates.append((i, j))

if __name__ == "__main__":
    N, L, R = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    candidates = deque([(i, j) for i in range(N) for j in range(i%2, N, 2)])
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    day = 0
    while True:
        for _ in range(len(candidates)):
            i, j = candidates.popleft()
            if visited[i][j] != day:
                visited[i][j] = day
                find_union(i, j)
                 
        if len(candidates) == 0:
            break
        day += 1
    
    print(day)