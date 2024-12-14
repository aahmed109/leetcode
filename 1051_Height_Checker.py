class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exp = heights.copy()
        exp.sort()       
        p=0
        for i in range(len(exp)):
            if heights[i] != exp[i]:
                p+= 1
            
        return p
