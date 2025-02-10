class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original): return []
        res = []

        i = 0
        j = 0
        while i < m:
            res.append(original[j:j+n])
            i += 1
            j += n

        return res
