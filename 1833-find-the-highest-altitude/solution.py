class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        l = [0,]
        for num in gain:
            alt += num
            l.append(alt)
        return max(l)

        
