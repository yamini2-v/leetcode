class Solution:
    def isHappy(self, n: int) -> bool:
      s = set()
      while n > 1 and n not in s:
        s.add(n)
        n= sum(int(digit)**2 for digit in str(n))
      return n == 1

