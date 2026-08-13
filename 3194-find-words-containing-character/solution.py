class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        l = []
        for i,j in enumerate (words):
            if x in j:
                l.append(i)
        return l
        
