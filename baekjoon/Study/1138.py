import sys
input = sys.stdin.readline
num_person = int(input())
nums_high_left = list(map(int, input().split()))
lines = [0] * num_person

for person, num_high_left in enumerate(nums_high_left, start=1):
    for i in range(len(lines)):
        if not num_high_left and lines[i] == 0:
            lines[i] = person
            break
            
        if lines[i] == 0:
            num_high_left -= 1
        
print(*lines)