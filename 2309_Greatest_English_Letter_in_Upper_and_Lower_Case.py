class Solution:
    def greatestLetter(self, s: str) -> str:
        ans = ""
        se = set()
        for l in s:
            if ord(l) >= 97 and ord(l) <= 122:
                if chr(ord(l)-32) in s:
                    se.add(chr(ord(l)-32))
        li = list(se)

        if len(li) == 1:    # kinda unnecessary optimisation
            ans += li[0]
            return ans

        m = -1

        for l in li:
            if ord(l) > m:
                m = ord(l)
        if m > 0: ans += chr(m)
        return ans
