class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        avg = []
        nums.sort()
        s = 0
        e = len(nums) - 1
        while s < e:
            avg.append((nums[s]+nums[e])/2) 
            s += 1
            e -= 1
        return len(set(avg))
