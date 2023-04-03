from typing import List

# Solution 1. Using 'sort' built-in function
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums should have 0 ~ len(nums)
        if 0 not in nums:
            return 0
        if len(nums) not in nums:
            return len(nums)

        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > 1:
                return nums[i]+1
            
# Solution 2. Gauss Formular
# nums should have had 0 ~ len(nums) and it’s sum is (len(nums) * (len(nums)+1)).
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # The missing number is the result of (Gauss sum) - (current sum).
        return (len(nums) * (len(nums)+1)) // 2 - sum(nums)
    
# Solution 3. Bit Manipulation
# A bitwise XOR operation between same values will output 0.
from functools import reduce
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # The result will be the missing number.
        return reduce(lambda x, y: x ^ y, list(range(len(nums)+1)) + nums, 0) 
    