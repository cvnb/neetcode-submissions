class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([ char for char in s if char.isalnum()]).lower()
        r = s[::-1]
        return s == r
        