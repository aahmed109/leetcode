class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        res = 0

        for w in words1:
            if w in words2 and words1.count(w) == 1 and words2.count(w) == 1:
                res += 1

        return res
