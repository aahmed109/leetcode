class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3: return s
        res = ""
        res += s[0:2]
        print(res)
        i = 2
        while i < len(s):
            if s[i-2] != s[i-1]:
                res += s[i]
            elif s[i-1] == s[i-2]:
                if  s[i-1] != s[i]:
                    res += s[i]
                
            i+=1

        return res
