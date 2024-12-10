class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i=0
        while i<len(nums)-1:
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
            i+=1

        for j in range(len(nums)):
            if nums[j] == 0:
                nums.remove(0)
                nums.append(0)

        return nums
