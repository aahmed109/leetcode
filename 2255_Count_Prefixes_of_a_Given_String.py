class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        res = 0
        for i in range(len(words)):
            if words[i] == s[:len(words[i])]:
                res += 1

        return res
