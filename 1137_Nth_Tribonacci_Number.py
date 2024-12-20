class Solution:
    def tribonacci(self, n: int) -> int:
        ans = [0,1,1]
        if n < 3: return ans[n]
        i = 3
        while i <= n:
            ans.append(ans[i-3]+ans[i-2]+ans[i-1])
            i+=1

        return ans[n]
