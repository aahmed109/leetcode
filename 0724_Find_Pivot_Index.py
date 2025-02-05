class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ts = sum(nums)
        ls = 0
        for i in range(len(nums)):
            rs = ts - ls - nums[i]
            if ls == rs:
                return i
            ls += nums[i]
        return -1
