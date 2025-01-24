class Solution:
    def shift(self, c: str, x: int) -> str:
        return chr((ord(c)+x-97)%26+97)
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res = [None]*len(s)
        i = len(s)-1
        val = 0
        while i >= 0:
            val += shifts[i]
            res[i] = self.shift(s[i], val)
            i -= 1
        return ''.join(res)
