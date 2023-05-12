import sys
input = sys.stdin.readline

passwd = input().rstrip()
vowels = ['a', 'e', 'i', 'o', 'u']

def check_acceptable(passwd):
        stack = list(passwd)
        c_cnt, v_cnt = 0, 0 # constant / vowel counter
        last_ch = '' # a char popped from stack
        v_flag = 0 # a flag to check whether any vowel is used or not
        
        while stack:
            last_ch = stack.pop()
            if last_ch in vowels:
                v_flag = 1
                c_cnt, v_cnt = 0, v_cnt + 1
            else: 
                c_cnt, v_cnt = c_cnt + 1, 0
            
            # check if same char comes 2 times continuosly or
            # check if constant or vowel comes 3 times continuosly
            if (stack and (last_ch == stack[-1]) and (last_ch not in ('e', 'o'))) or v_cnt == 3 or c_cnt == 3:
                return False
        
        # check if there is not any vowel in password
        return True if v_flag == 1 else False
    
while passwd != 'end':
    print(f"<{passwd}> is acceptable." if check_acceptable(passwd) else f"<{passwd}> is not acceptable.")
    passwd = input().rstrip()