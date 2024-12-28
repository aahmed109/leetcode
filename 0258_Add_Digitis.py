class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            n = num
            t = 0
            while n != 0:
                t += n%10
                n = n // 10

            num = t

        return num
