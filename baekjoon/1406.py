import sys
input = sys.stdin.readline
string, M = input().rstrip(), int(input())

l_stack, r_stack = list(string), [] # l_stack은 커서 왼쪽에 있는 문자열, r_stack은 커서 오른쪽에 있는 문자열
for _ in range(M):
    command = input().split()
 
    if command[0] == 'L' and l_stack:
        r_stack.append(l_stack.pop())
    elif command[0] == 'D' and r_stack:
        l_stack.append(r_stack.pop())
    elif command[0] == 'B' and l_stack:
        l_stack.pop()
    elif command[0] == 'P':
        l_stack.append(command[1])

ans = ''.join(l_stack) + ''.join(reversed(r_stack)) # r_stack은 반대로 저장되어 있음
# 주의: r_stack.reverse()는 r_stack이 비어있을 시 에러 발생
print(ans)