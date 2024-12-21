class Solution:
    def getascii(self, char: str) -> int:
        return ord(char)-64

    def titleToNumber(self, columnTitle: str) -> int:
        i=0
        tot = 0
        while i < len(columnTitle):
            tot += self.getascii(columnTitle[i])*26**(len(columnTitle)-1-i)
            i+=1
        
        return tot
