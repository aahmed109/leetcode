class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        k={}
        m = -1
        rs=0
        n = len(nums)
        for i in range(n):
            k[i] = nums[i]
            rs += nums[i]

        for i in range(n):
            if i+1 not in k.values():
                m=i+1
                break
        
        su = int((n*(n+1)/2))
        d = rs+m-su

        return [d,m]
