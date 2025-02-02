class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        res = []
        sCol = ord(s[0])
        sRow = int(s[1])
        eCol = ord(s[3])
        eRow = int(s[4])

        i = sCol
        

        while i <= eCol:
            j = sRow
            while j <= eRow:
                res.append(chr(i)+str(j))
                j += 1
            i += 1
        return res
