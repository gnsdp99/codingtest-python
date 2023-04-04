# Solution 1. Bit Manipulation
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) + (n & 1)
            n >>= 1
        return res
    
# Solution 2. String Operation
class Solution:
    def reverseBits(self, n: int) -> int:
        bits = bin(n)[2:]
        bits = '0'*(32 - len(bits)) + bits
        return int(bits[::-1], 2)