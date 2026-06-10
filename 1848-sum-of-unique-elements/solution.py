class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        t = 0
        for (k,v) in count.items():
            if v == 1:
                t += k
        return t
