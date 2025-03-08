class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        return rle(self.countAndSay(n - 1))

def rle(s: str) -> str:
    previous = s[0]
    count = 0

    encoded = ""

    for c in s:
        if c == previous:
            count += 1
        else:
            encoded = encoded + str(count) + previous
            count = 1
            previous = c

    encoded = encoded + str(count) + previous

    return encoded
