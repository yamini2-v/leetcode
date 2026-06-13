class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = []
        for word in words:
            tot = 0
            for ch in word:
                tot += weights[ord(ch) - ord('a')]
            value = tot % 26
            char =  chr(ord('z') - value)
            res.append(char)
        return''.join(res) 




        
