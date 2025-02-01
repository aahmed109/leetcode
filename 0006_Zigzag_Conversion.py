class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res = []
        for i in range(numRows):
            res.append("")

        rev = False
        i = j = 0
        while i < len(s):
            res[j] += s[i]
            i += 1
            if not rev:
                if j == numRows - 1:
                    j -= 1
                    rev = True
                else: j += 1
            else:
                if j == 0:
                    j += 1
                    rev = False
                else: j -=1

        return ''.join(res)
