# 백준 14890 경사로 (G3)
def check_slope(section):
    return section.count(section[0]) == len(section)

def check_available(line):
    if line.count(line[0]) == len(line):
        return True
    
    i = 0
    while i < N-1: 
        if abs(line[i] - line[i+1]) >= 2:
            return False
        if line[i] > line[i+1]:
            if i+L >= N:
                return False
            if not check_slope(line[i+1:i+L+1]):
                return False
            else:
                i = i+L
            if i < N-1 and (line[i] < line[i+1] or not check_slope(line[i+1:i+L+1])):
                return False
        elif line[i] < line[i+1]:
            if i-L+1 < 0:
                return False
            if not check_slope(line[i-L+1:i+1]):
                return False
            else:
                i += 1
        else:
            i += 1
    return True

if __name__ == "__main__":
    N, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    num_road = 0
    for i in range(N):
        # 가로
        num_road += check_available(board[i])
        # 세로
        col = list(zip(*board))[i]
        num_road += check_available(col)
    print(num_road)