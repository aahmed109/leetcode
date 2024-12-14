class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        Max = -1
        lMax = 0
        zerocount = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                lMax+=1
            else:
                zerocount +=1

                if lMax > Max:            
                    Max = lMax        
                lMax = 0
            if i == len(nums)-1:
                if lMax > Max: Max = lMax
        return Max
