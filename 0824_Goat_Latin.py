class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel = "aeiouAEIOU"
        consonant = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        li = sentence.split()
        res = ""
        i = 1
        for word in li:
            if word[0] in vowel:
                word += "ma"
            elif word[0] in consonant:
                c = word[0]
                word = word[1:]
                word += c+"ma"
            word += "a"*i
            i+=1
            res += word +" "
        res = res[:len(res)-1]
        return res
