class Solution:
    k = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    v = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    m = dict(zip(k, v))

    def frequency(self, s: str) -> tuple[()]:        
        k = [0] * 26
        for c in s:
            k[self.m[c]] += 1
        return tuple(k)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for s in strs:
            k = self.frequency(s)
            if k in group:                
                group[k].append(s)
            else:
                group[k] = [s]

        return list(group.values())

        