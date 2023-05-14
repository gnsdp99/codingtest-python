import sys
input = sys.stdin.readline
nums = [int(input()) for _ in range(int(input()))]

# bubble sort
for i in range(len(nums)-1, 0, -1):
    for j in range(0, i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

for i in range(len(nums)):
    print(nums[i])