# 백준 11053 가장 긴 증가하는 부분 수열 (S2)
if __name__ == "__main__":
    # # 방법 1
    # N = int(input().strip())
    # A = [0] + list(map(int, input().split()))
    # dp = [0] + [1] * N
    
    # for i in range(2, N+1):
    #     for j in range(1, i):
    #         if A[i] > A[j]:
    #             dp[i] = max(dp[i], dp[j] + 1)
    # print(max(dp))
    
    
    # 방법 2
    N = int(input().strip())
    A = list(map(int, input().split()))
    sequence = [A[0]]

    for num in A:
        if sequence[-1] < num:
            sequence.append(num)
        else:
            for i, seq_num in enumerate(sequence):
                if num <= seq_num:
                    sequence[i] = num
                    break
    print(len(sequence))