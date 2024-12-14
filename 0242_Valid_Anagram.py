class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        q = list(set(s))
        r = list(set(t))
        q.sort()
        r.sort()
        for i in range(len(q)):
            if q[i] != r[i]:
                return False

        ht = {}
        for c in q:
            ht[c] = s.count(c)

        for i in ht.keys():
            if t.count(i) != ht[i]:
                return False

        return True
