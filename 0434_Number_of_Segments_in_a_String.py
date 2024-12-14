class Solution:
    def countSegments(self, s: str) -> int:
        if s.strip() == "": return 0
        t=s.strip()
        return len(t.split())
