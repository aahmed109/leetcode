class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        mini = 9999
        nums.sort()
        s = 0
        e = len(nums) - 1
        while s < e:
            mini = min(mini, (nums[s]+nums[e])/2) 
            s += 1
            e -= 1
        return mini
