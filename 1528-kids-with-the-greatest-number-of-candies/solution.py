class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l = []
        for i in candies:
            s = i+ extraCandies
            l.append(s >= max(candies))
        return l
        
        
