class Solution:
    def defangIPaddr(self, address: str) -> str:
        res = ""
        li = address.split(".")
        for ad in li:
            res += ad+"[.]"

        return res[:(len(res)-3)]
