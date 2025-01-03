class Solution:
    def maxScore(self, s: str) -> int:
        m = -1
        i = 1
        while i < len(s):
            ls = s[:i]
            rs = s[i:]
            lt = ls.count("0")+rs.count("1")
            m = max(m, lt)
            i += 1
        return m
