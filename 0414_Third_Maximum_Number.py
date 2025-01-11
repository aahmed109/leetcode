# O(nlogn) solution
#class Solution:
#    def thirdMax(self, nums: List[int]) -> int:
#        n=list(set(nums))
#        if len(n) >= 3:
#            n.sort(reverse=True)
#            return n[2]

#        else:
#            return max(n)

# O(n) Solution
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n=list(set(nums))
        
        if len(n) >= 3:
            for i in range(2):
                n.remove(max(n))

        return max(n)
