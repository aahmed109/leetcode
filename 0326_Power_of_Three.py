class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        num = 0
        while pow(3,num) <= n:
            if pow(3,num) == n:
                return True
            num+=1

        return False
