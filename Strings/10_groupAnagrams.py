class Solution:

    def groupAnagrams(self,str):

        d = {}

        for s in str:
            key = tuple(sorted(s))
            d[key] = d.get(key,[]) + [s]
        return d.values()

solution = Solution()

str = ["eat","tea","tan","ate","nat","bat"]

print(solution.groupAnagrams(str))