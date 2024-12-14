class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num={}
        n=-99999
        for i in range(len(nums)):
            if nums[i] in num.values():
                #print(i)
                num.update({nums[i]: -99999})
                #n=-99999
            else:
                num.update({nums[i]: nums[i]})
                #n=nums[i]
		k=num.values()
        for i in k:
            if i != -99999:
                return i
