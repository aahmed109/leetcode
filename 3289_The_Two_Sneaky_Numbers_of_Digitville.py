class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        num = set(nums)
        sn = []
        for i in num:
            if nums.count(i) > 1:
                sn.append(i)

        return sn
