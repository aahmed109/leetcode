class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        i = commands.count("DOWN") - commands.count("UP")
        j = commands.count("RIGHT") - commands.count("LEFT")

        return (i * n) + j
