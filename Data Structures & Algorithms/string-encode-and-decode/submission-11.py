class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "EMPTYLIST"
        else:
            return chr(28).join(strs)


    def decode(self, s: str) -> List[str]:
        if s == 'EMPTYLIST':
            return []
        else:
            return s.split(chr(28))
