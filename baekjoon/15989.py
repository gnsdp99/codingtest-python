# 풀이 1. 재귀를 이용한 조합 풀이 (시간 초과)
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

# def combination_n(n):
#     def recur(curr_comb, curr_sum):
#         global num_case
#         if curr_sum == n:
#             num_case += 1
#             return
#         elif curr_sum > n:
#             return
        
#         for i in (1, 2, 3):
#             if not curr_comb or curr_comb[-1] <= i:
#                 curr_comb.append(i)
#                 recur(curr_comb, curr_sum+i)
#                 curr_comb.pop()
    
#     recur([], 0)

# if __name__ == "__main__":
#     for _ in range(int(input())):
#         num_case = 0
#         combination_n(int(input()))
#         print(num_case)
        
        
# 풀이 2. DP (답 참조)
import sys
input = sys.stdin.readline
        
if __name__ == "__main__":
    # dp[i]는 1, 2, 3의 합으로 i를 만드는 경우의 수
    # i는 모두 1의 합으로 만들 수 있음.
    dp = [1] * 10_001
    
    # dp[i]는 dp[i-2]의 각 경우에 +2를 한 것과 같음.
    for i in range(2, 10_001):
        dp[i] += dp[i-2]

    # dp[i]는 dp[i-3]의 각 경우에 +3을 한 것과 같음.
    for i in range(3, 10_001):
        dp[i] += dp[i-3]
        
    for _ in range(int(input())):
        print(dp[int(input())])