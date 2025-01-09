class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        c = 0
        while x != 0 or y != 0:
            x_shifted = x & ((1 << 1) - 1)
            y_shifted = y & ((1 << 1) - 1)
            if x_shifted != y_shifted: c += 1
            x >>= 1
            y >>= 1

        return c
