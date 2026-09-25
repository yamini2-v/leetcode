class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        l = []
        
        for m in matrix:
            s = 0
            for i in m:
                s += i
            l.append(s)
        return l
        