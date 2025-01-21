class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        i = 0
        for s in arr:
            if arr.count(s) == 1:
                i += 1
                if i == k:
                    return s

        return ""
