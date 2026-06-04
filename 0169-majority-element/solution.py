class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = len(nums)
        t = l / 2
        d = dict() 
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        for (k,v) in d.items():
            if v > t:
                return k

