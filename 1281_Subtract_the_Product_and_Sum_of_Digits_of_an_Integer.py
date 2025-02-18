class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = 0
        m = 1

        while n != 0:
            s += n%10
            m *= n%10
            n //= 10
        return m-s
