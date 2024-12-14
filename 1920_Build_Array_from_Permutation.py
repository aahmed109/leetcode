class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        num = []
        for i in range(len(nums)):
            num.append(nums[nums[i]])

        return num
