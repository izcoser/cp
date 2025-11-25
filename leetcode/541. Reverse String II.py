class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        out = ""

        start = 0
        end = 2 * k
        len_s = len(s)

        while True:
            chunk = s[start:end]
            if not chunk:
                break
            out += reverse_chunk(chunk, k)
            start += 2 * k
            end += 2 * k

        return out

def reverse_chunk(chunk: str, k: int) -> str: # reverse chunks of less than 2k characters.
    s = chunk
    len_s = len(s)
    if len_s < k:
        return s[::-1]
    if len_s >= k:
        return s[:k][::-1] + s[k:]
