class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0
        s = 1
        e = x
        while s<=e:
            m = (s+e)//2
            if m * m == x: return m
            elif m * m > x:
                e = m -1
            else: s = m + 1

        return e
