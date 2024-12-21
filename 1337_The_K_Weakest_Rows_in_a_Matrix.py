class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = {}

        for r in range(len(mat)):
            ans[r] = mat[r].count(1)

        sd = sorted(ans.items(), key=lambda kv: (kv[1], kv[0])) #sort dictionary by value
        
        ret = [sd[i][0] for i in range(k)]

        return ret
