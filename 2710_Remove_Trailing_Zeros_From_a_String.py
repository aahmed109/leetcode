class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        i = len(num)-1
        while i >= 0:
            if num[i] != '0':
                return num[:i+1]
            i -= 1
