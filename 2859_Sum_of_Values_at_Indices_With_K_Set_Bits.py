class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        s = 0
        for i in range(len(nums)):
            if list(bin(i)).count('1') == k:
                s+= nums[i]
        return s
