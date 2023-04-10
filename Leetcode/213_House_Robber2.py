# Sol 1. Dynamic Programming - Bottom-up
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_house(houses: List[int]) -> int:
            # dp[i] means the maximum amount of money at houses[:i+1]
            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(dp[0], houses[1])

            for i in range(2, len(houses)):
                dp[i] = max(dp[i-1], dp[i-2]+houses[i])
        
            return dp[-1]

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        return max(rob_house(nums[1:]), rob_house(nums[:-1]))