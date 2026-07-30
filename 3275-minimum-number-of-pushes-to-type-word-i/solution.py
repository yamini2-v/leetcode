class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        if n <= 8:
            return n
        else:
            j = word[:8]
            k = word[8:16]
            l = word[16:24]
            m = word[24:26]
            return len(j)*1 + len(k)*2 + len(l)*3 + len(m)*4

        
