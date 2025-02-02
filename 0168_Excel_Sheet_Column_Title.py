class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""
        i = 0
        n = columnNumber
        while n > 26:
            m = n % 26
            if m == 0:
                m = 26
                n-=1
            res += chr(m+64)
            
            n //= 26
        if n > 0:
            res += chr(n+64)
        return res[::-1]
