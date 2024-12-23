class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        se = set()
        for l in word:
            if ord(l) >= 97 and ord(l) <= 122:
                if chr(ord(l)-32) in word:
                    se.add(chr(ord(l)-32))
        
        return len(se)
