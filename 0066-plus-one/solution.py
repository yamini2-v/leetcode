class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
      r = 0
      for i in digits:
        r = r * 10 + i
      r += 1 
      s = [int(i) for i in str(r)]
      return s
