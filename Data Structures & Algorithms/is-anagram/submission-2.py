class Solution:
    def frequency(self, s: str) -> {}:
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        return d

    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = self.frequency(s)
        t_dict = self.frequency(t)

        return bool(s_dict == t_dict)



        
        