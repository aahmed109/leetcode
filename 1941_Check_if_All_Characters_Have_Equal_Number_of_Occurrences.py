class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        se = set(list(s))
        c = s.count(s[0])
        for a in se:
            if s.count(a) != c:
                return False
        return True
