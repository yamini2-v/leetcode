class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        s = set(candyType)
        t = len(s)
        n = len(candyType)//2
        return min(t,n)


        