# 백준 17140 이차원 배열과 연산 (G4)
from collections import Counter      
def operation_row(arr):
    max_len = 0
    for i in range(len(arr)):
        counts = sorted(Counter([k for k in arr[i] if k != 0]).items(), key=lambda x:(x[1], x[0]))
        new_row = [k for j in range(len(counts)) for k in counts[j]]
        arr[i] = new_row
        max_len = max(max_len, len(new_row))
    # 최대 길이만큼 0으로 채우기
    for i in range(len(arr)):
        while len(arr[i]) != max_len:
            arr[i].append(0)
        
def transpose(arr):
    transpose_arr = [col for col in list(zip(*arr))]
    return transpose_arr

if __name__ == "__main__":
    R, C, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(3)]
    def solution(arr):
        # 100초간 실행
        for t in range(101):
            num_row, num_col = len(arr), len(arr[0])
            if len(arr) >= R and len(arr[0]) >= C and arr[R-1][C-1] == K:
                return t
            if num_row >= num_col:
                operation_row(arr)
            else:
                arr = transpose(arr)
                operation_row(arr)
                arr = transpose(arr)
        return -1
    
    ans = solution(arr)
    print(ans)