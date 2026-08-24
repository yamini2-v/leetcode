class Solution:
    def countAsterisks(self, s: str) -> int:
        slant = 0
        astrix = 0
        for i in s:
            if i == '|':
                slant += 1
            elif slant % 2 == 0 and i == '*':
                astrix += 1
        return astrix
        