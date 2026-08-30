class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        l = len(nums)
        x = min(nums)
        y = max(nums)
        if x == y:   
            return 1

        f = max(nums.index(x), nums.index(y)) + 1
        b = max(l - nums.index(x), l - nums.index(y))
        m = nums.index(x) + 1 + (l - nums.index(y))
        n = nums.index(y) + 1 + (l - nums.index(x))

        return min(f, b, m, n)
