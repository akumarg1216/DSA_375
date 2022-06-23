class Solution:
    def longestCommonPrefix(self, strs):
        result = ""       
        for n in zip(*strs):
            print(strs)
            print(n)
            if len(set(n)) == 1:
                result += n[0]
            else:
                return result
        return result
        
solution = Solution()

strs = ["flight","flap","flow","fly"]

print(solution.longestCommonPrefix(strs))