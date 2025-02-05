class Solution:
    def findLetter(self, c: str) -> bool:
        if (ord(c) >= 97 and ord(c) <= 122) or (ord(c) >= 65 and ord(c) <= 90):
            return True
        return False

    def reverseOnlyLetters(self, s: str) -> str:
        i = 0
        j = len(s) - 1
        while i < j:
            if self.findLetter(s[i]) == False:
                i += 1
            elif self.findLetter(s[j]) == False:
                j -= 1
            else:
                s = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
                i += 1
                j -= 1

        return s
