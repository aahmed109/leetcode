class Solution:
    def findTotal(self, n: int) -> int:
        return (n*(n+1)//2)
    def pivotInteger(self, n: int) -> int:
        if n == 1: return n
        ts = self.findTotal(n)
        
        n -= 1
        while n > 0:
            ps = self.findTotal(n)
            
            if ts - ps + n == ps:
                return n
            n -= 1

        if sq**2 == ts: return sq
        return -1

    ##Prefix Sum

    def pivotInteger(self, n: int) -> int:
    
        ts = self.findTotal(n)
        sq = int(sqrt(ts))

        if sq**2 == ts: return sq
        return -1
