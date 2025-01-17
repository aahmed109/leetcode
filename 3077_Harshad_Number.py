class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        n = x
        ds = 0
        while n > 0:
            ds += n %10
            n//=10
        if x%ds != 0: return -1

        return ds
