class Solution:
    def countAsterisks(self, s: str) -> int:
        res = 0
        inp = False
        i = 0
        while i < len(s):
            if s[i] == '|':
                inp = not inp
            elif s[i] == '*' and not inp:
                res += 1
            i += 1
        return res
