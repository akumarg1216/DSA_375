class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            print(i)
            print("S[i] ",s[i])
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            print("MaxLength: ",maxLength)
            usedChar[s[i]] = i
            print("Used Char: ",usedChar)
            print("====================================")

        return maxLength

solution = Solution()

s = "abcabcbb"

print(solution.lengthOfLongestSubstring(s))
