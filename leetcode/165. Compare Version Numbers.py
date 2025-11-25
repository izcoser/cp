class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # make both versions have the same number of revisions
        revisions_1 = version1.count(".")
        revisions_2 = version2.count(".")

        diff = abs(revisions_1 - revisions_2)
        if revisions_1 > revisions_2:
            version2 += ".0" * diff
        else:
            version1 += ".0" * diff

        # compare values left to right
        vals1 = version1.split(".")
        vals2 = version2.split(".")

        for i in range(len(vals1)):
            a = int(vals1[i])
            b = int(vals2[i])
            if a > b:
                return 1
            elif a < b:
                return -1

        return 0