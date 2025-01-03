class Solution:
    def isBalanced(self, num: str) -> bool:
        i = 0
        s = 0
        for letter in num:
            n = int(letter)
            if i % 2 == 0: s+=n
            else: s-=n

            i += 1

        return s == 0
