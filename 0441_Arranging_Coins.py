class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int(sqrt(2*n+.25)-.5))
