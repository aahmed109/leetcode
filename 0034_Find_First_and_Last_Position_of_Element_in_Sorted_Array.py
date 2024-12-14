class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0: return [-1,-1]
        if len(nums) ==  1: 
            if nums[0] == target: return [0,0]
            else: return [-1, -1]

        s=0
        e=len(nums)-1
        res = [-1,-1]
        while s <= e:
            m = (s+e)//2
            #print(m)
            #print(s,e)
            if nums[m] == target:
                i=s
                c=0
                counter = 0
                while i <= e:
                    if nums[i] == target:
                        if c < 1:
                            c = 1
                            res[0] = i
                        else: counter +=1
                    i+=1
                res[1] = res[0]+counter
                return res
            elif nums[m] < target:
                s = m+1
            else:
                e = m-1

        return res
