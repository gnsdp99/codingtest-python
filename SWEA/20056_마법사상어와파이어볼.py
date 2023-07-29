# 백준 20056 마법사 상어와 파이어볼 (G4)
from collections import defaultdict
def move_fireball():
    fireballs = []
    for (r, c) in board:
        for m, s, d in board[(r, c)]:
            nr = (r + s * dx[d]) % N
            nc = (c + s * dy[d]) % N
            fireballs.append((nr, nc, m, s, d))
    return fireballs

def make_board(fireballs):
    board = defaultdict(list)
    for r, c, m, s, d in fireballs:
        board[(r, c)].append((m, s, d))
    return board

def divide_fireball():
    new_board = defaultdict(list)
    for (r, c) in board:
        sum_mass, sum_speed = 0, 0
        num_odd, num_even = 0, 0
        for m, s, d in board[(r, c)]:
            sum_mass += m
            sum_speed += s
            if d % 2 == 0:
                num_even += 1
            else:
                num_odd += 1
        if (num_even + num_odd) > 1:
            divided_mass = (sum_mass) // 5
            if divided_mass == 0:
                continue
            divided_speed = (sum_speed) // (num_even + num_odd)
            for i in range(4):
                new_direction = i * 2 if num_odd == 0 or num_even == 0 else 2 * i + 1
                new_board[(r, c)].append((divided_mass, divided_speed, new_direction))
        else:
            new_board[(r, c)] += board[(r, c)]
    return new_board

if __name__ == "__main__":
    N, M, K = map(int, input().split())
    fireballs = [list(map(int, input().split())) for _ in range(M)]
    board = make_board(fireballs)
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
        
    for _ in range(K):
        fireballs = move_fireball()
        board = make_board(fireballs)
        board = divide_fireball()
    sum_mass = sum([m for (r, c) in board for m, s, d in board[(r, c)]])
    print(sum_mass)