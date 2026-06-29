class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)        
        counter =  0

        for n in s:
            if (n - 1) not in s:
                c = 0
                while n in s:
                    c += 1
                    n += 1                
                counter = max(counter, c)
        
        return counter


