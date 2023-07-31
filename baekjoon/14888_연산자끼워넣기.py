# 백준 14888 연산자 끼워넣기 (S1)
def backtrack(curr_res, num_to_select):
    global max_res, min_res
    if num_to_select == 0:
        if max_res < curr_res:
            max_res = curr_res
        if min_res > curr_res:
            min_res = curr_res
        return
    
    for i, num_rest in enumerate(ops):
        if num_rest > 0:
            ops[i] -= 1
            if i == 0:
                backtrack(curr_res + numbers[(num_ops+1) - num_to_select], num_to_select - 1)
            elif i == 1:
                backtrack(curr_res - numbers[(num_ops+1) - num_to_select], num_to_select - 1)
            elif i == 2:
                backtrack(curr_res * numbers[(num_ops+1) - num_to_select], num_to_select - 1)
            elif i == 3:
                backtrack(((-1) *curr_res) // numbers[(num_ops+1) - num_to_select] * (-1), num_to_select - 1) if curr_res < 0 else backtrack(curr_res // numbers[(num_ops+1) - num_to_select], num_to_select - 1)
            ops[i] += 1

if __name__ == "__main__":
    N = int(input().strip())
    numbers = list(map(int, input().split()))
    ops = list(map(int, input().split()))
    
    max_res, min_res = float('-inf'), float('inf')
    num_ops = sum(ops)
    backtrack(numbers[0], num_ops)
    
    print(f'{max_res}\n{min_res}')