class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = str(n)
        tot = 0
        cng = 1
        for i in range(len(s)):
            tot += cng*int(s[i])
            cng *= -1

        return tot
