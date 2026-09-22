class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'
        def string(word):
            if len(word) >= k:
                return word[k-1]
            else:
                for ch in word:
                    z = chr(ord(ch)+1)
                    word = word + z
                return string(word)
        return string(word)