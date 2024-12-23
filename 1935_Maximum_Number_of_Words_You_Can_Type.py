class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        t = text.split()
        res = len(t)
        for l in brokenLetters:
            i=0
            while i < len(t):
                if l in t[i]:
                    t.remove(t[i])
                    res -=1
                else:
                    i+=1
        
        return res
