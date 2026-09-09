class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        s = []
        d = []
        for num in nums:
            if len(str(num)) == 1:
                s.append(num)
            else:
                d.append(num)
        return sum(s) != sum(d)
            