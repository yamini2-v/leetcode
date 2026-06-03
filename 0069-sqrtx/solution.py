class Solution:
    def mySqrt(self, x: int) -> int:
        from math import sqrt
        s = sqrt(x)
        return floor(s)
        
