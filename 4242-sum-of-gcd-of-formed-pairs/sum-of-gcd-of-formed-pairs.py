class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        p = []
        n = 0
        for i in range(len(nums)):
            n = max(nums[i],n)
            s = gcd(n,nums[i])
            p.append(s)
        m = sorted(p)
        z = 0
        l = 0
        r = len(m)-1
        while l<r:
            z += gcd(m[l],m[r])
            l += 1
            r -= 1
        return z



        