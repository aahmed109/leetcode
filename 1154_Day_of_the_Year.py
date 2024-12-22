class Solution:
    def ifLeap(self, year: int) -> bool:
        if year % 400 == 0 or (year % 100 != 0 and year % 4 ==0):
            return True
        return False

    def dayOfYear(self, date: str) -> int:
        mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        li = date.split("-")
        forms = []
        for d in li:
            forms.append(int(d))

        ans = forms[2]
        #print(forms[1])
        if self.ifLeap(forms[0]) and forms[1] > 2:
            ans += 1
        
        for d in range(forms[1]-1):
            ans += mon[d]

        return ans
