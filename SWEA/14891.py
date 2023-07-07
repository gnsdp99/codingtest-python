# 14891 톱니바귀 G5
def rotate(n_cog, clockwise):
    if clockwise == 1:
        cogwheels[n_cog] = cogwheels[n_cog][7] + cogwheels[n_cog][:7]
    else:
        cogwheels[n_cog] = cogwheels[n_cog][1:8] + cogwheels[n_cog][0]
        
def chaining_rotate(left_cog, right_cog, me, clockwise):
    if left_cog < 1 or right_cog > 4:
        return
    
    if cogwheels[left_cog][2] != cogwheels[right_cog][6]:
        if me == 'left':
            chaining_rotate(right_cog, right_cog+1, 'left', clockwise*(-1))
            rotate(right_cog, clockwise*(-1))
        else:
            chaining_rotate(left_cog-1, left_cog, 'right', clockwise*(-1))
            rotate(left_cog, clockwise*(-1))    
        
def calculate_score():
    score = 0
    for i in range(1, 5):
        if cogwheels[i][0] == '1':
            score += 2**(i-1)
    return score

if __name__ == "__main__":
    cogwheels = [''] + [input().rstrip() for _ in range(4)]
    for _ in range(int(input())):
        left, right = 0, 0
        
        n_cog, clockwise = map(int, input().split())
        if n_cog in (1, 2, 3):
            chaining_rotate(n_cog, n_cog+1, 'left', clockwise)
        if n_cog in (2, 3, 4):
            chaining_rotate(n_cog-1, n_cog, 'right', clockwise)
            
        rotate(n_cog, clockwise)
            
    print(calculate_score())