class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        
        while nums[0] == 0:
            nums.remove(0)
            if len(nums) == 0: break
        return len(set(nums))
