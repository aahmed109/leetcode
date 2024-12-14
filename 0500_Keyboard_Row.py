class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        ans = []
        for word in words:
            w = word.lower()
            if len(set(keyboard[0]+w)) == len(keyboard[0]) or len(set(keyboard[1]+w)) == len(keyboard[1]) or len(set(keyboard[2]+w)) == len(keyboard[2]):
                ans.append(word)

        return ans
