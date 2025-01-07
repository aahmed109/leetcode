class Solution:
    def hammingWeight(self, n: int) -> int:
        c = 0
        while n != 0:
            m = n & ((1 << 1) - 1)

            if m == 1: c+=1
            n >>= 1
        return c
