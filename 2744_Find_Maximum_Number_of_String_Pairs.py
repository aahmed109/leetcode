class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        res = 0
        i = 0

        while i < len(words):
            j = i+1
            while j < len(words):
                if words[i] == words[j][::-1]:
                    res += 1
                    words.remove(words[i])
                    i -= 1
                    j -= 1
                    words.remove(words[j])
                    break
                else:
                    j += 1
            i += 1

        return res
