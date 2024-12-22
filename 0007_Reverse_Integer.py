class Solution:
    def reverse(self, x: int) -> int:
        minus = x < 0
        xstr = str(x)
        if minus:
            xstr = xstr[1:]
        li = list(xstr)
        li.reverse()

        res = ""
        for i in li:
            res += i
        numres = int(res)
        if numres > 2**31-1: return 0
        if minus: numres *= -1

        return numres
