class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        res = ""
        i = 0
        while i < min(len(strs[0]), len(strs[1])):
            if strs[0][i] == strs[1][i]:
                res += strs[0][i]
            else: break
            i+=1

        for i in range(2, len(strs)):
            res = res[:len(strs[i])]
            if res == "": break   
            j = 0
            while j < len(res):
                if strs[i][j] != res[j]:
                    res = res[:j] + res[j+1:] #remove character at index j
                else:
                    j+=1

        return res
