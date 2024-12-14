class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        s = 0

        while i < len(nums):
            s+=nums[i]
            i+=2
        return s
