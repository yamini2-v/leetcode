class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        l = []
        for word in words:
            char = word.lower()
            for row in rows:
                if all(ch in row for ch in char):
                    l.append(word)
                    break
        return l






        
