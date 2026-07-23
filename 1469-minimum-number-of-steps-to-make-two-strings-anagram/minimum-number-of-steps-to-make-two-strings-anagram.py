class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sum = 0
        a = Counter(s)
        b = Counter(t)
        for k in a.keys():
            if a[k] > b[k]:
                sum += abs(a[k]- b[k])
        return sum
           
        