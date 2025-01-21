class Solution:
    def minimumChairs(self, s: str) -> int:
        res = 0
        stack = []
        for i in s:
            if i == "E":
                stack.append(i)
            else:
                stack.pop()
            res = max(res, len(stack))
        return res
