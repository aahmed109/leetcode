class Solution:
    def capitalizeTitle(self, title: str) -> str:
        ans = ""
        li = title.split()
        for word in li:
            word = word.lower()
            if len(word) > 2:
                word = chr(ord(word[0])-32)+word[1:]
                
            ans += word + " "

        return ans[:len(ans)-1]
