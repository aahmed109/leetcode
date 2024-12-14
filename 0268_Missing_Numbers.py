class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        rs = int((n*(n+1)/2))
        s=0
        i=0
        while i<len(nums):
            s+=nums[i]
            i+=1
        return rs-s 
