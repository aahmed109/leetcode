class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        mi = []
        for i in range(2):
            mi.append(min(nums))
            nums.remove(min(nums))
        for i in range(2):
            mi.append(max(nums))
            nums.remove(max(nums))

        return mi[3]*mi[2] - mi[1]*mi[0]
