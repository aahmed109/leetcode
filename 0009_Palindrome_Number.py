class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        s = str(x)
        print(s)
        if len(s) == 1: return True
        if len(s) == 2:
            return s[0] == s[1]
        t = s[:(len(s)//2)]
        t = t[::-1]
        mid = -1
        if len(s) % 2 == 0:
            mid = len(s)//2
        else:
            mid  = len(s)//2 + 1
        if t == s[mid:]:
                return True
        else:
            return False
