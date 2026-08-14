class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s = set()
        c = Counter(arr)
        for (k,v) in c.items():
            if v in s:
                return False
            else:
                s.add(v)
        return True
        