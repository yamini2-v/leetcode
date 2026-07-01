class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        m = s.split( )
        return ' '.join(m[:k])
