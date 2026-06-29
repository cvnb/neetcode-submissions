class Solution:
    def charFrequency(self, s: str) -> {}:
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        return d

    def isAnagram(self, s: str, t: str) -> bool:
        s_freq = self.charFrequency(s)
        t_freq = self.charFrequency(t)

        return s_freq == t_freq
        