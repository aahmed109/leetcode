class Solution:
    def findNext(self, nums: List[int], n: int) -> int:
        for i in range(len(nums)):
            if nums[i] > n: return nums[i]
        return -1

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge={}
        for i in range(len(nums2)-1):
            ss = nums2[i+1:len(nums2)]

            nge[nums2[i]] = self.findNext(ss, nums2[i])

        nge[nums2[len(nums2)-1]] = -1

        for i in range(len(nums1)):
            nums1[i] = nge[nums1[i]]

        return nums1
