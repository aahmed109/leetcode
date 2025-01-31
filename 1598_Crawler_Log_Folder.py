class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = []
        for log in logs:
            if log == "../":
                if res: res.pop()
            elif log == "./":
                continue
            else:
                res.append(log)
        return len(res)
