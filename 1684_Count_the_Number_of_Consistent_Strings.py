class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = len(words)
        for word in words:
            wordlist = list(set(list(word)))
            for letter in wordlist:
                if letter not in allowed:
                    c -= 1
                    break

        return c
