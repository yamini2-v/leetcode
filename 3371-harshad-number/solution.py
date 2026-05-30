class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        temp = x
        s = 0
        while temp > 0:
            d = temp % 10
            s += d
            temp //= 10
        if x % s == 0:
          return s    
        else:
            return -1
