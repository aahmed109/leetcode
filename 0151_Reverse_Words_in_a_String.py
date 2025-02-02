class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        l = s.split()
        for word in l:
            word = word.strip()
        l = l[::-1]
        return ' '.join(l)
