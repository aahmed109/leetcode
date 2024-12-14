class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s=0
        st=0
        for i in nums:
            if i<10:
                s+=i
            else:
                st+=i

        return st!=s
