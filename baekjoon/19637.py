import sys
input = sys.stdin.readline
N, M = map(int, input().split())
GRADES = [] # (칭호, 상한값)
for _ in range(N):
    temp = input().split()
    if GRADES and int(temp[1]) == GRADES[-1][1]:
        continue
    else:
        GRADES += [(temp[0], int(temp[1]))]

def binary_search(value):
    # 이분 탐색
    left, right = 0, len(GRADES)-1
    while left <= right:
        mid = left + (right - left) // 2
        # mid가 0일때와 아닐때로 나뉨.
        if mid == 0:
            # mid가 0일 때는 무조건 [0]인덱스와 [1]인덱스 중 하나가 답임
            return GRADES[0][0] if value <= GRADES[0][1] else GRADES[1][0]
        
        if GRADES[mid-1][1] < value <= GRADES[mid][1]:
            return GRADES[mid][0]
        elif value <= GRADES[mid-1][1]:
            right = mid - 1
        elif value > GRADES[mid][1]:
            left = mid + 1
    
    # 답이 없는 경우
    return -1

for _ in range(M):
    print(binary_search(int(input())))