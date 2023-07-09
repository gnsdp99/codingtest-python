# 15686 치킨 배달 (G5)
def get_combinations(coords, num_to_select):
    combinations = []
    if num_to_select == 0:
        return [[]]

    for i, fixed in enumerate(coords):
        rest = coords[i+1:]
        for comb in get_combinations(rest, num_to_select - 1):
            combinations.append([fixed] + comb)
    return combinations

def get_distance(starts, goals):
    dist = 0
    for s_x, s_y in starts:
        temp = float('inf')
        for g_x, g_y in goals:
            temp = min(temp, abs(g_x - s_x) + abs(g_y - s_y))
        dist += temp
    return dist 

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    coord_of_houses = [(i, j) for i in range(N) for j in range(N) if board[i][j] == 1]
    coord_of_chickens = [(i, j) for i in range(N) for j in range(N) if board[i][j] == 2]

    combinations = get_combinations(coord_of_chickens, M)
    
    min_dist = float('inf')
    for comb in combinations:
        min_dist = min(min_dist, get_distance(coord_of_houses, comb))
    print(min_dist)