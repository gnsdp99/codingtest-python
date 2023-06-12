# 문제 1065. 한수 (S4)
import sys
input = sys.stdin.readline

def find_num_hansu(max_num):
    num_hansu = 99 if max_num >= 100 else max_num
    for num in range(100, max_num+1):
        str_num = str(num)
        diff = int(str_num[1]) - int(str_num[0])
        is_hansu = 1
        for i in range(1, len(str_num)-1):
            if int(str_num[i+1]) - int(str_num[i]) != diff:
                is_hansu = 0
                break
        
        num_hansu += 1 if is_hansu else 0
    return num_hansu
            
if __name__ == "__main__":
    print(find_num_hansu(int(input())))