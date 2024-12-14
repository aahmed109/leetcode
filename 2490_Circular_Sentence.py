class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        last = words[len(words)-1]
        if words[0][0] != last[len(last)-1]: return False

        res = True
        
        for i in range(len(words)-1):
            #print(i)
            if words[i][len(words[i])-1] != words[i+1][0]:
                res = False
                break
        return res
