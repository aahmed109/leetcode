class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: return False
        num = 0
        while pow(4,num) <= n:
            if pow(4,num) == n:
                return True
            num+=1

        return False
