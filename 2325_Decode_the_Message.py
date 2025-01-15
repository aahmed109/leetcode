class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = dict()
        i = 0
        for c in key:
            if c not in d.keys() and ord(c) != 32:
                d[c] = chr(i+97)
                i += 1

        res = ""

        for c in message:
            if ord(c) == 32:
                res += " "
            else: res += str(d.get(c))
        return res
