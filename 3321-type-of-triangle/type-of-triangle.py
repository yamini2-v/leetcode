class Solution:
    def triangleType(self, nums: List[int]) -> str:
            a, b, c = sorted(nums)
            if a + b <= c:
                return "none"

            s = len(set(nums))
            if s == 1:
                return 'equilateral'
            elif s == 2:
                return 'isosceles'
            else:
                return 'scalene'
            