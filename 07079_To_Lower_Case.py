class Solution:
    def toLowerCase(self, s: str) -> str:
        for i in range(len(s)):
            if s[i].upper() == s[i]:
                s = s [:i] + s[i].lower() + s[i+1:]

        return s
