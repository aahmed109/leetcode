class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a = s1.split()
        b = s2.split()
        q=0
        s=0

        unc = []
        res = []
        c=len(a)
        while s<len(a):
            if a.count(a[s])>1:
                rr = a[s]
                res.append(rr)
                i=a.count(rr)
                while i>0:
                    a.remove(rr)
                    i-=1       
            else: s+=1

        s=0
        while s<len(b):
            if b.count(b[s])>1:
                rr = b[s]
                res.append(rr)
                i=b.count(rr)
                while i>0:
                    b.remove(rr)
                    i-=1       
            else: s+=1

        for s in b:
            if s not in a and s not in res:
                unc.append(s)
        for s in a:
            if s not in b and s not in res:
                unc.append(s)
        return unc
