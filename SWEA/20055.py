# 20055 컨베이어 벨트 위의 로봇 (G5)
from collections import deque
def is_zero(loc):
    global num_zero
    num_zero += 1 if A[loc] == 0 else 0
    
def unload_robot():
    if conveyor[loc_unloading]:
        conveyor[loc_unloading] = 0
        
def rotate():
    unload_robot()
    A.appendleft(A.pop())
    conveyor.appendleft(conveyor.pop())
    unload_robot()

def move_robot():
    for i in range(loc_unloading-1, -1, -1):
        if conveyor[i] and not conveyor[i+1] and A[i+1]:
            conveyor[i+1], conveyor[i] = 1, 0
            A[i+1] -= 1
            is_zero(i+1)
            
def load_robot():
    if A[loc_loading]:
        conveyor[loc_loading] = 1
        A[loc_loading] -= 1
        is_zero(loc_loading)

if __name__ == "__main__":
    N, K = map(int, input().split())
    A = deque(list(map(int, input().split())))
    conveyor = deque([0] * (2 * N))  # 0: empty, 1: robot
    loc_loading, loc_unloading = 0, N - 1
    
    num_zero = 0
    num_process = 0
    while num_zero < K:
        rotate()
        move_robot()
        load_robot()
        num_process += 1
        
    print(num_process)