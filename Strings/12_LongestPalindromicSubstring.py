class Solution:

    def longestPalindromicSubdstring(self,s):
        count=0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if (s[i:j]) == s[i:j][::-1]:
                    count = count +1
        return count


s = "aaaaaa"

solution = Solution()

print(solution.longestPalindromicSubdstring(s))
