# Solution 1. Dynamic Programming
from collections import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = [0]
        for i in range(1, n+1):
            if i % 2 == 1: # odd
                counts.append(counts[i-1] + 1)
            else: # even
                counts.append(counts[i//2])

        return counts
    
# Solution 2. 'count' built-in function
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [bin(i).count('1') for i in range(n+1)]
        return ans