class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)        
        max_seq_ctr =  0

        for n in s:
            if (n - 1) not in s:
                seq_ctr = 0
                while n in s:
                    seq_ctr += 1
                    n += 1                
                max_seq_ctr = max(max_seq_ctr, seq_ctr)
        
        return max_seq_ctr


