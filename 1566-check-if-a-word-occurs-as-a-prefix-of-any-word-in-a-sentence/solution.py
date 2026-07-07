class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        l = sentence.split()
        for i in l:
          if i.startswith(searchWord):
            n = l.index(i)
            return n+1
        return -1

