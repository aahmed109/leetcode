class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        return max(moves.count("R"), moves.count("L")) + moves.count("_") - min(moves.count("R"), moves.count("L"))
