import sys
input = sys.stdin.readline
N, M = int(input()), int(input())
x = list(map(int, input().split())) # 가로등이 설치될 위치

def find_height(x):
    # 가로등이 하나인 경우
    if len(x) == 1:
        return max(x[0], N - x[0])
    
    # 첫 번째 가로등이 최소 0까지는 비춰야 함.
    height = x[0]
    for x_i, x_j in zip(x, x[1:]):
        # 가로등의 높이 h는 두 가로등의 위치 x1, x2에 대해 (x2 - x1) <= 2*h가 성립해야 함.
        temp = ((x_j - x_i) // 2) if (x_j - x_i) % 2 == 0 else ((x_j - x_i) // 2) + 1
        height = max(height, temp)
    # 마지막 가로등이 최소 N - x[-1] 까지는 비춰야 함.
    height = max(height, N - x[-1])
    return height
    
print(find_height(x))