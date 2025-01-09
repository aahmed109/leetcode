class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        m = list(s)
        r = [None]*len(s)

        i = 0
        while i < len(m):
            r[indices[i]] = m[i]
            i+=1

        return ''.join(r)
