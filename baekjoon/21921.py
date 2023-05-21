import sys
input = sys.stdin.readline
N, X = map(int, input().split())
num_visitors = list(map(int, input().split()))

def find_max_visitor():
    curr_sum = sum(num_visitors[:X])
    max_sum = curr_sum
    cnt = 1
    for i in range(1, N-X+1):
        curr_sum = curr_sum - num_visitors[i-1] + num_visitors[i+X-1]
        if curr_sum == max_sum:
            cnt += 1
        elif curr_sum > max_sum:
            cnt = 1
            max_sum = curr_sum

    return max_sum, cnt
    
num, cnt = find_max_visitor()
print("SAD") if num == 0 else print(f"{num}\n{cnt}")