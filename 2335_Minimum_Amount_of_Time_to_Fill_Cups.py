class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        if amount[0]+amount[1] <= amount[2]: return amount[2]
        c = 0
        while amount[0] + amount[1] > amount[2]:
            amount[0] -= 1
            amount[1] -= 1
            c += 1

        return amount[2] + c
