class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m = 0
        for sentence in sentences:
            l = len(sentence.split())
            m = max(m,l)
        return m

        