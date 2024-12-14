class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        r = -9999
        for i in sentences:
            s = len(i.split())
            if s>r:
                r = s

        return r
