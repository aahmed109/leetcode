# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1: return n
        s = 1
        e = n
        #m=-1
        while s < e:
            m = s+((e-s)//2)
            if isBadVersion(m):
                e = m
            else:
                s = m+1
        return s
