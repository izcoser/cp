class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        d_reverse = {}
        words = s.split()
        i = 0

        if len(pattern) != len(words):
            return False
            
        for p in pattern:
            if p in d:
                if d[p] == words[i] and d_reverse[words[i]] == p:
                    i += 1
                    continue
                else:
                    return False
            else:
                if words[i] in d_reverse:
                    return False

                d[p] = words[i]
                d_reverse[words[i]] = p
            i += 1
        return True