class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words_in_sentence = sentence.split()
        for index, w in enumerate(words_in_sentence):
            if w.startswith(searchWord):
                return index + 1
        return -1
        