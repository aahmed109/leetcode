class Solution:
    def countPoints(self, rings: str) -> int:
        n = len(rings)
        if n < 6: return 0
        res = 0
        d = dict()
        for i in range(10):
            d[i] = set()
        i = 0

        while i < n:
            clr = rings[i]
            num = int(rings[i+1])
            d[num].add(clr)
            
            i += 2
        for i in range(10):
            if len(d[i]) == 3:
                res += 1

        return res
