class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]*(n+1)
        for i in range(1,len(res)):
            res[i] = (i % 2) + res[i//2]
            
        return res
