class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        cc = 0
        s=0

        #unc = []
        res = []

        while s<len(words1):
            if words1.count(words1[s])>1:
                rr = words1[s]
                res.append(rr)
                i=words1.count(rr)
                while i>0:
                    words1.remove(rr)
                    i-=1       
            else: s+=1

        s=0
        while s<len(words2):
            if words2.count(words2[s])>1:
                rr = words2[s]
                res.append(rr)
                i=words2.count(rr)
                while i>0:
                    words2.remove(rr)
                    i-=1       
            else: s+=1

        print(words1)
        print(words2)
        for s in words2:
            if s in words1 and s not in res:
                cc+=1
				
        return cc
