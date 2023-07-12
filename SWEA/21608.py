# 백준 21608 상어 초등학교 (G5)
def locate_with_rules(no_student):
    max_like, max_space = 0, 0
    loc_x, loc_y = rest_loc[0]
    for x, y in rest_loc:
        num_like, num_space = 0, 0
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < N and 0 <= new_y < N:
                if not board[new_x][new_y]:
                    num_space += 1
                elif board[new_x][new_y] in students[no_student]:
                    num_like += 1
        if num_like > max_like or (num_like == max_like and num_space > max_space):
            loc_x, loc_y = x, y
            max_like, max_space = num_like, num_space

    rest_loc.remove((loc_x, loc_y))
    return loc_x, loc_y

def get_score(x, y):
    num_like = 0
    no_student = board[x][y]
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < N and 0 <= new_y < N:
            if board[new_x][new_y] in students[no_student]:
                num_like += 1
    
    return int(10 ** (num_like - 1))

if __name__ == "__main__":
    N = int(input().strip())
    students = dict()
    for _ in range(N*N):
        no_student, *likes = map(int, input().split())
        students[no_student] = likes
    board = [[0] * N for _ in range(N)]
    rest_loc = [(i, j) for i in range(N) for j in range(N)]
    
    for no_student in students:
        loc_x, loc_y = locate_with_rules(no_student)
        board[loc_x][loc_y] = no_student
        
    total_score = 0
    for x in range(N):
        for y in range(N):
            total_score += get_score(x, y)
    print(total_score)