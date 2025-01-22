class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] >= 0 or nums[-1] <= 0: return -1
        i = len(nums)-1
        while i > 0:
            if nums[i]*(-1) in nums:
                return nums[i]
            i -=1
        return -1
