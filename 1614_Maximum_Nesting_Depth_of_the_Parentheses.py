class Solution:
    def maxDepth(self, s: str) -> int:
        res = -9999
        #i = 0
        #while i < len(s):
        #    if s[i] != '(' and s[i] != ')':
        #        s = s[:i] + s[i+1:]
        #    else: i += 1
        s = ''.join([char for char in s if char in '()']) #Thanks ChatGPT
        if len(s) == 0: return 0
        k=0

        lres = 0
        while k < len(s):
            if s[k] == ')': 
                k+=1
                lres -= 1
                continue

            while s[k] == '(':
                k+=1
                lres+=1
            res = max(res, lres)
        
        return res
