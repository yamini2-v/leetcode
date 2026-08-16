class Solution:
    def maxFreqSum(self, s: str) -> int:
        z = ['a','e','i','o','u']
        co = 0
        vo = 0
        c = Counter(s)
        for (k,v) in c.items():
            if k in z:
                vo=max(vo,v)
            else:
                co = max(co,v)
        return co+vo
        
