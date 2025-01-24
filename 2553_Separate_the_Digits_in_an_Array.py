class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            l = list(str(num))
            for digit in l:
                res.append(int(digit))
        return res
