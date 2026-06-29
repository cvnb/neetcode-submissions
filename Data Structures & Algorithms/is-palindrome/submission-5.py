"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([ char for char in s if char.isalnum()]).lower()
        r = s[::-1]
        return s == r
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = [char.lower() for char in s if char.isalnum()]
        
        l = 0
        r = -1
        n = len(x) // 2

        while n != 0:
            if x[l] != x[r]:
                return False
            
            l += 1
            r -= 1
            n -= 1
        
        return True