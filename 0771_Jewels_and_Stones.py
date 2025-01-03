class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        l1 = list(jewels)
        l2 = list(list(stones))
        print(l1)
        print(l2)
        for stone in l2:
            if stone in l1:
                res += 1

        return res
