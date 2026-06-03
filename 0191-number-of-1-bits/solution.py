class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)
        c = b.count(str(1))
        return c
