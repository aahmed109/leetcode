class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        s = set(nums)
        c = 0
        for i in s:
            q = nums.count(i)
            c+= (int) (q*(q-1)/2)

        return c
