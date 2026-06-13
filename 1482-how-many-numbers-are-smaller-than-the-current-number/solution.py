class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s = sorted(nums)
        l = []
        for i in nums:
           b = s.index(i)
           l.append(b)
        return l
           

        
