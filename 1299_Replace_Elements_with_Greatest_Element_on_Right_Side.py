class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1]
        i = len(arr)-2
        m = arr[len(arr)-1]
        while i >= 0:
            res.insert(0, max(m,arr[i+1]))
            m = max(m,arr[i+1])
            i -= 1
        return res
