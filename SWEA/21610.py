# 백준 21610 마법사 상어와 비바라기 (G5)
def increase_water(clouds):
    global water
    for x, y in clouds:
        water[x][y] += 1
        
def move_clouds(direction, s):
    global clouds, visited, N
    for i, (x, y) in enumerate(clouds):
        new_x = (N + x + direction[0] * s) % N
        new_y = (N + y + direction[1] * s) % N
        clouds[i] = (new_x, new_y)
        visited[new_x][new_y] = 1
    increase_water(clouds)

def check_diagonal():
    global clouds, water
    diagonals = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
    for x, y in clouds:
        for dx, dy in diagonals:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(water) and 0 <= new_y < len(water):
                if water[new_x][new_y]:
                    water[x][y] += 1

def make_clouds():
    global clouds, water, visited
    new_clouds = []
    for x in range(len(water)):
        for y in range(len(water)):
            if not visited[x][y] and water[x][y] >= 2:
                new_clouds.append((x, y))
                water[x][y] -= 2
    return new_clouds

def get_total_water(water):
    total_water = 0
    for x in range(len(water)):
        total_water += sum(water[x])
    return total_water

if __name__ == "__main__":
    N, M = map(int, input().split())
    water = [list(map(int, input().split())) for _ in range(N)]
    clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
    directions = [(), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    for _ in range(M):
        d, s = map(int, input().split())
        visited = [[0] * N for _ in range(N)]
        move_clouds(directions[d], s)
        check_diagonal()
        clouds = make_clouds()
    print(get_total_water(water))