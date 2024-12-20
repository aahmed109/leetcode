class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cng = [0,0,0]
        for money in bills:
            if money == 5: cng[0] += 1
            elif money == 10:
                cng[1] += 1
                cng[0] -= 1

            else: 
                cng[2] += 1
                cng[0] -= 1
                if cng[1] > 0: cng[1] -= 1
                else: cng[0] -= 2
            if cng[0] < 0 or cng[1] < 0 or cng[1] < 0: return False

        return True
