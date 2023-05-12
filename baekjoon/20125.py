import sys
input = sys.stdin.readline

N = int(input()) # size of plane
# cookie = [list(input().rstrip()) for _ in range(N)]
cookie = [input().rstrip() for _ in range(N)]

# find heart first
for i in range(len(cookie)):
    j = cookie[i].find('*')
    if j != -1:
        heart_y, heart_x = i+1, j
        break

# should add 1 to coordinate
print(f"{heart_y+1} {heart_x+1}")
    
limbs = [0 for _ in range(5)] # left arm, right arm, waist, left leg, right leg

# length of arms
idx = cookie[heart_y].index('*')
for j in range(idx, len(cookie)):
    if cookie[heart_y][j] != '*':
        break
    if j < heart_x:
        limbs[0] += 1
    elif j > heart_x:
        limbs[1] += 1
            
# legth of waist
for i in range(heart_y+1, len(cookie)):
    if cookie[i][heart_x] == '*':
        limbs[2] += 1
    else:
        break

# length of legs
for i in range(heart_y+limbs[2]+1, len(cookie)):
    if cookie[i][heart_x-1] == '*':
        limbs[3] += 1
    if cookie[i][heart_x+1] == '*':
        limbs[4] += 1
    if cookie[i][heart_x-1] != '*' and cookie[i][heart_x+1] != '*':
        break
    
print(*limbs)