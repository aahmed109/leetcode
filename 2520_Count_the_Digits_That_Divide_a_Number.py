class Solution:
    def countDigits(self, num: int) -> int:
        ntoa = list(str(num))
        c=0
        for n in ntoa:
            k = int(n)
            if num%k == 0:
                c += 1
        return c
