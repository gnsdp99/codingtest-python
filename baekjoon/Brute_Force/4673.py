# 문제 4673. 셀프 넘버 (S5)
import sys
input = sys.stdin.readline

def find_dn(MAX_RANGE):
    for num in range(1, MAX_RANGE):
        temp = num
        for n in str(num):
            temp += int(n)
        if temp <= 10000:
            self_num_list[temp] = 0

if __name__ == "__main__":
    MAX_RANGE = 10_001
    self_num_list = [1] * MAX_RANGE
    find_dn(MAX_RANGE)

    for num in range(1, MAX_RANGE):
        if self_num_list[num] == 1:
            print(num)