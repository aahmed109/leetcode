class Solution:
    def isValid(self, s: str) -> bool:
        op = ["(", "{", "["]
        cl = [")", "}", "]"]
        stack = []
        if s[0] in cl or len(s)%2 == 1: return False
        for c in s:
            if c in op: stack.append(c)
            else:
                if len(stack) == 0: return False
                if op[cl.index(c)] == stack[-1]: stack.pop()
                else: stack.append(c)
            #print(stack)
        
        return len(stack) == 0
