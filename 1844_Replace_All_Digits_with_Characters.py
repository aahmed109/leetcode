class Solution:
    def shift(self, c: str, x: int) -> str:
        return chr(ord(c)+x)
    def replaceDigits(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            if i%2 == 0: res += s[i]
            else:
                res += self.shift(s[i-1], int(s[i]))
        return res
