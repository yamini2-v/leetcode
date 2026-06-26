class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        p = []
        l = 0
        r = n
        while l < n :
            p.append(nums[l])
            p.append(nums[r])
            l += 1
            r += 1
        return p
        
