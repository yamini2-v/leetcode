class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        l = []
        s = s1 + ' ' + s2
        words = s.split()
        count = Counter(words)
        for k,v in count.items():
            if v == 1:
                l.append(k)
        return l

        
