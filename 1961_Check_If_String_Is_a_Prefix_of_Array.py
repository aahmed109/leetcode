class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        t = ""
        for i in range(len(words)):
            t += words[i]
            if t == s:
                return True
        return False
