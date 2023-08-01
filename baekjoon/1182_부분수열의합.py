# 백준 1182 부분수열의 합 (S2)
def backtrack(start, curr_sum, num_selected):
    global ans
    if curr_sum == S and num_selected >= 1:
        ans += 1
    
    for i in range(start, N):
        backtrack(i+1, curr_sum + numbers[i], num_selected + 1)

if __name__ == "__main__":
    N, S = map(int, input().split())
    numbers = list(map(int, input().split()))
    ans = 0
    
    backtrack(0, 0, 0)
    print(ans)