import sys
input = sys.stdin.readline
N = int(input())
budgets = sorted(list(map(int, input().split())))
M = int(input()) # total budget

def find_maxBudget():
    num_remain = N # 남은 예산 개수
    bud_remain = M # 남은 할당 가능한 예산
    
    if sum(budgets) <= bud_remain:
        return budgets[-1]
    
    max_budget = bud_remain // num_remain
    for i in range(N-1):
        temp = (bud_remain - budgets[i]) // (num_remain - 1)
        if temp >= budgets[i]: # 다음 할당할 예산이 이전 할당한 예산 이상이어야 함.
            num_remain -= 1
            bud_remain -= budgets[i] 
            max_budget = temp
        else:
            return max_budget

    return max_budget

print(find_maxBudget())