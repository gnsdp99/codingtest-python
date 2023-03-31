from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        
        ans = 0
        while left < right:
            if height[left] <= height[right]:
                amount = (right - left) * height[left]
                left += 1
            else:
                amount = (right - left) * height[right]
                right -= 1
                
            ans = max(ans, amount)
            
        return ans

sol = Solution()
height = list(map(int, input().split(',')))
print(sol.maxArea(height))