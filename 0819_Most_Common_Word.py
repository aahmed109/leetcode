import string

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        res = []
        tr = paragraph.maketrans(string.punctuation, ' '*len(string.punctuation)) #replace all punctuation with space
        
        rp = paragraph.translate(tr)
        li = rp.split()
        for word in li:
            if word not in banned:
                res.append(word.lower())
        
        s = set(res)
        print(res)
        print(s)
        m = -1
        ret = ""
        for word in s:
            if res.count(word) > m:
                ret = word
                m = res.count(word)
        return ret
