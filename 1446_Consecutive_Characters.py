class Solution:
    def maxPower(self, s: str) -> int:
        i = 0
        p = 1
        po = 1
        while i < len(s)-1:
            if s[i] == s[i+1]:
                p+=1
                po = max(p,po)
            else:
                p=1
            i+=1 

        return po
