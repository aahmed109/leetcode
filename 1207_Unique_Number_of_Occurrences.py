class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s = set(arr)
        c = []
        for a in s:
            if arr.count(a) in c: return False
            c.append(arr.count(a))
        return True
