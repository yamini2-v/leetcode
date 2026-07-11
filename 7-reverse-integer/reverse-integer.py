class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        r = 0
        while x > 0:
            n = x % 10
            r = r * 10 + n * sign
            x = x // 10
        if r < -2**31 or r > 2**31-1:
            return 0
        return r


        