class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        p = 1
        num = n
        while num > 0:
            d = num%10
            s += d
            p *= d
            num = num//10
        return n % (s+p) == 0
            

        