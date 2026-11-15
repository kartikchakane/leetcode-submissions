class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nSet = set(nums)
        longest = 0

        for x in nSet:
            if x-1 in nSet:
                continue

            current , length = x ,1

            while current +1 in nSet:
                length +=1
                current +=1

            longest = max(length ,longest)

        return longest
        

        