class Solution:
    def getSum(self, nums: List[int]) -> int:
        s = 0
        for a in nums:
            s += a
        return s

    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        if k == 1:
            return self.getSum(nums) - 2*min(nums)

        nums.sort()
        
        if nums[0] <= 0:
            i=0
            while i < k:
                if i == len(nums):
                    nums.sort()
                    k = k - i
                    i = 0
                    continue
                if nums[i] <= 0:
                    nums[i] *= -1
                    i += 1
                else:
                    mini = min(nums[i], nums[i-1])

                    mini = mini*((-1)**(k-i))

                    if mini > 0: return self.getSum(nums)
                    return self.getSum(nums)+2*mini
            
        else:
            nums[0] = nums[0]*(-1)**k

        return self.getSum(nums)
