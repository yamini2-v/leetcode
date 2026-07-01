class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        s = Counter(nums)
        return sorted(nums,key=lambda x:(s[x],-x))      
