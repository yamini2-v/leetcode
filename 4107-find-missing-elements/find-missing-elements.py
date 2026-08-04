class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = sorted(nums)
        l = []
        for i in range(s[0],s[-1]+1):
            if i not in nums:
                l.append(i)
        return l
        