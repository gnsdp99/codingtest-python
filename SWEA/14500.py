# 백준 14500 테트로미노 (G4)
def rotate(tetromino, times):
    for i in range(times):
        temp = list(zip(*tetromino[i]))
        new_tetromino = []
        for j in range(len(temp)):
            new_tetromino.append(list(temp[j])[::-1])
        tetromino.append(new_tetromino)
        
def reverse(tetromino):
    for i in range(len(tetromino)):
        new_tetromino = []
        for j in range(len(tetromino[i])):
            new_tetromino.append(tetromino[i][j][::-1])
        tetromino.append(new_tetromino)
        
def make_tetromino_L(tetromino):
    rotate(tetromino, 3)
    reverse(tetromino)
        
def make_tetromino_S(tetromino):
    rotate(tetromino, 1)
    reverse(tetromino)
    
def make_tetromino_T(tetromino):
    rotate(tetromino, 3)
    
def place_on_board(tetromino):
    global board
    N, M, K, L = len(board), len(board[0]), len(tetromino), len(tetromino[0])
    max_score = 0
    for i in range(N):
        for j in range(M):
            if 0 <= i <= N - K and 0 <= j <= M - L:
                temp_score = 0
                for p in range(K):
                    for q in range(L):
                        temp_score += tetromino[p][q] * board[i+p][j+q]
                max_score = max(max_score, temp_score)
                
    return max_score

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    tetromino_I = [[[1, 1, 1, 1]], [[1], [1], [1], [1]]]
    tetromino_O = [[[1, 1], [1, 1]]]
    tetromino_L = [[[1, 0], [1, 0], [1, 1]]]
    make_tetromino_L(tetromino_L)
    tetromino_S = [[[1, 0], [1, 1], [0, 1]]]
    make_tetromino_S(tetromino_S)
    tetromino_T = [[[1, 1, 1], [0, 1, 0]]]
    make_tetromino_T(tetromino_T)
    
    answer = 0
    for tetromino in [tetromino_I, tetromino_O, tetromino_L, tetromino_S, tetromino_T]:
        for one_tetromino in tetromino:
            answer = max(answer, place_on_board(one_tetromino))
    
    print(answer)