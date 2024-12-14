class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        num = []
        for i in range(len(words)):
            if x in words[i]:
                num.append(i)

        return num
