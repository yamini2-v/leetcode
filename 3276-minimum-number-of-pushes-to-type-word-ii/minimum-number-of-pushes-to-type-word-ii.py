class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        n = len(word)
        p = 0
        if n <= 8:
            return n
        else:
            z = sorted(c.values(),reverse=True)
            for i,k in enumerate(z):
                mul = i // 8 + 1
                p += k * mul
                  

            return p

        