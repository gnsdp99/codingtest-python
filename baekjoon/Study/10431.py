import sys
input = sys.stdin.readline

P = int(input())

for _ in range(P):
    T, *heights = map(int, input().split()) # * is unpacking operator
    
    cnt = 0
    # insertion sort
    for i in range(1, len(heights)):
        for j in range(i, 0, -1):
            if heights[j] < heights[j-1]:
                heights[j], heights[j-1] = heights[j-1], heights[j]
                cnt += 1
            else:
                break              

    print(T, cnt)