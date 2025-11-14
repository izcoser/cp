class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        s = ''.join([i for i in s.lower() if i.isalnum() ])
        print(s)

        len_s = len(s)
        for i in range(0, len_s // 2):
            if s[i] != s[len_s - i - 1]:
                return False
        return True