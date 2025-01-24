class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mini = min(len(word1), len(word2))
        res = [None]*2*mini
        
        j = 0
        for i in range(len(res)):
            if i%2 == 0:
                res[i] = word1[j]
            else:
                res[i] = word2[j]
                j += 1

        if len(word1) > len(word2):
            return ''.join(res)+word1[j:]
        elif len(word1) < len(word2):
            return ''.join(res)+word2[j:]
        else:
            return ''.join(res)
