class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        co = 0
        f = s[0]
        for c in range(len(s)):
            if s[c] == f:
                stack.append(s[c])
            else:
                if len(stack) != 0:
                    stack.pop()
                    if len(stack) == 0:
                        co += 1
                        f = s[(c+1)%len(s)]
        return co
