class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0: return []
        if len(nums) == 1: return [str(nums[0])]
        res = []
        i = 0
        while i < len(nums):
            f = str(nums[i])
            j = i+1
            while j< len(nums):
                if nums[i] + 1 == nums[j]:
                    i+=1
                    j+=1
                else:
                    break
            e = str(nums[j-1])
            if f == e: res.append(f)
            else: res.append(f+"->"+e)
            i += 1

        return res
