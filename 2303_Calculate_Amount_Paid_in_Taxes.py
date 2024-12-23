class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = min(income, brackets[0][0]) * (brackets[0][1] / 100)
        income -= min(income, brackets[0][0])

        for i in range(1, len(brackets)):

            less = min(income, brackets[i][0] - brackets[i - 1][0])
            tax += less * (brackets[i][1] / 100)
            income -= less

            if income == 0:
                break

        return tax
