class Solution:
    def sortSentence(self, s: str) -> str:
        l = s.split()
        res = [None]*len(l)
        for word in l:
            res[int(word[-1])-1] = word[:-1]
        return ' '.join(res)
