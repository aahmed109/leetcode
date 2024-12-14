class Solution:
    def compressedString(self, word: str) -> str:
        comp=""
        i=0
        while i<len(word):
            c = word[i]
            cnt = 0
            while i<len(word) and cnt <9 and word[i] == c:
                cnt+=1
                i+=1
            comp += str(cnt)+c

        return comp
        
