# LeetCode 125.Valid Palindrome (Easy)

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_copy = s[:]
        s_copy = s_copy.lower()
        s_copy = s_copy.replace(' ', '')
        s_copy = re.sub('[^a-zA-Z0-9]', '', s_copy)
        return s_copy == s_copy[::-1]