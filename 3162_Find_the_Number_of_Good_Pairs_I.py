class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        s=0
        q=[]
        for i in range(len(nums2)):
            q.append(nums2[i]*k)
        #print(q)
        for i in range(len(nums1)):
            for j in range(len(q)):
                if nums1[i]%q[j]==0:
                    #print(i, j)
                    s+=1

        return s
