class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        j = len(words)-1
        while j >= 0:
            l = words[len(words)-1].split(separator)
            words.pop()

            i = len(l)-1
            while i >= 0:
                if len(l[i]) > 0: words.insert(0, l[i])
                i-=1

            j -= 1
        return words
