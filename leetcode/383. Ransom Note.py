from collections import Counter
# easy, hash table
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for letter, count in ransom_count.items():
            if letter not in magazine_count or magazine_count[letter] < count:
                return False
        return True