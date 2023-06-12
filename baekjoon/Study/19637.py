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
        if value <= GRADES[mid][1]:
            right = mid - 1
        else:
            left = mid + 1
    return GRADES[left][0]

for _ in range(M):
    print(binary_search(int(input())))