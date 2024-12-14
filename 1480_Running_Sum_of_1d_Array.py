class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        ans.append(nums[0])
        for i in range(1, len(nums)):
            s=0
            for j in range(i+1):
                s+=nums[j]
            ans.append(s)

        return ans
