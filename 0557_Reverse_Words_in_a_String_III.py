class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        for w in range(len(l)):
            l[w] = l[w][::-1]
        return ' '.join(l)
