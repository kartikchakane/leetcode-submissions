from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map = Counter(s)

        for letter in t:
            s_map[letter] -= 1

        for count in s_map.values():
            if (count != 0):
                return False
        return True        




        