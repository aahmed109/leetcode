class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c=0
        for detail in details:
            m = detail[11]+detail[12]
            if int (m) > 60:
                c+=1

        return c
