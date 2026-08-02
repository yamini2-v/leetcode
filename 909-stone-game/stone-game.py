class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        a = []
        b = []
        l = 0
        r = len(piles)-1
        while l < r:
            a.append(max(piles[l],piles[r]))
            if piles[l] == max(piles[l],piles[r]):
                l += 1
            else:
                r-= 1
            b.append(min(piles[l],piles[r]))
            if piles[l] == min(piles[l],piles[r]):
                l += 1
            else:
                r -= 1
        return sum(a) > sum(b)
        