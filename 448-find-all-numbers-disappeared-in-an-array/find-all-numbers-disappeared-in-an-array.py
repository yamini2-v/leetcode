class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = set(nums)
        return [i for i in range(1,len(nums)+1) if i not in n]
                
        