class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        res = 1
        c = min(a,b)
        for i in range(2,c+1):
            if a%i ==  b%i == 0:
                res +=1
        return res
