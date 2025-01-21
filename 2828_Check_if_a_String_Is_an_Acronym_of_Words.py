class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return s == ''.join(p[0] for p in words if p)
