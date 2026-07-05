class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        for word in words:
            s = word[::-1]
            if s == word:
                return word
        else:
            return ''

        
