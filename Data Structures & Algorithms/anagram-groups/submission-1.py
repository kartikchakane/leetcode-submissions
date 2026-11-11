class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dct = {}

        for s in strs:
            x = ''.join(sorted(s))

            if x not in dct:
                dct[x] = [s]
            else:
                dct[x].append(s)

        return list(dct.values())
        