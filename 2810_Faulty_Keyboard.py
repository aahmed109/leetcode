class Solution:
    def finalString(self, s: str) -> str:
        i = 0
        while i < len(s):
            if s[i] == 'i':
                t = s[:i][::-1]

                s = t+s[i+1:]
            else:
                i += 1
        return s
