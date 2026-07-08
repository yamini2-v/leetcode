class Solution:
    def findLucky(self, arr: List[int]) -> int:
        l = []
        s = Counter(arr)
        for (k,v) in s.items():
            if k == v:
                l.append(k)
        return max(l) if l else -1

        
