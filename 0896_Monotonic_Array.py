class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        big = 1
        if nums[0] > nums[len(nums)-1]:
            big = -1
        if big == 1:
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    return False
        else:
            for i in range(len(nums)-1):
                if nums[i] < nums[i+1]:
                    return False
        return True
