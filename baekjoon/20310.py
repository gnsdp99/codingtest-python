import sys
input = sys.stdin.readline
S = input().rstrip()

# 전체 1의 개수 (남은 개수)
left_one = S.count('1')
# 새로운 문자열의 0과 1의 개수
num_zero, num_one = S.count('0') // 2, left_one // 2

new_S = '' # 새로운 문자열
for val in S:
    if val == '0' and num_zero: # 채워야할 0이 남았으면 무조건 채움
        new_S += val
        num_zero -= 1
    elif val == '1' and num_one:
        if num_one == left_one: # 앞으로 남은 1의 개수와 채워야 할 1의 개수가 같으면 채움 
            new_S += val
            num_one -= 1
        left_one -= 1
        
print(new_S)