class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        res = [None]*len(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies >= m:
                res[i] = True
            else:
                res[i] = False
        return res
