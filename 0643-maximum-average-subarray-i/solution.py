class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        c = 0
        for i in range(k):
            c += nums[i]
        mavg = c/k
        for i in range (k,n):
            c += nums[i]
            c -= nums[i-k]
            avg = c/k
            mavg = max(mavg,avg)
        return mavg
        

        
