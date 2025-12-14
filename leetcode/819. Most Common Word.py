from collections import defaultdict
from typing import List

# easy 
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = [i.lower() for i in banned]

        words = defaultdict(int)
        current_word_chars = []
        for ch in paragraph:
            if not ch.isalpha():
                if current_word_chars:
                    w = ''.join(current_word_chars)
                    words[w] += 1
                    current_word_chars = []
                else:
                    continue
            else:
                current_word_chars.append(ch.lower())
        
        if current_word_chars:
            w = ''.join(current_word_chars)
            words[w] += 1

        most_common = ""
        highest_freq = 0

        for word, freq in words.items():
            if freq > highest_freq and word not in banned:
                most_common = word
                highest_freq = freq
        return most_common


# from collections import Counter
# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         banned = set([i.lower() for i in banned])
#         words = [i for i in remove_all_non_alpha(paragraph.lower()).split()]
#         count = Counter(words)
#         most_common = words[0]
#         highest_freq = 0
#         for word, freq in count.items():
#             if freq > highest_freq and word not in banned:
#                 most_common = word
#                 highest_freq = freq
#         return most_common

# def remove_all_non_alpha(paragraph: str) -> str:
#     return ''.join([i if i.isalpha() else " " for i in paragraph])