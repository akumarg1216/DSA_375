import collections


class Solution:

    def characterReplacement(self, s, k):
        maxf = i = 0
        count = collections.Counter()
        for j in range(len(s)):
            print("count = ",count)
            count[s[j]] += 1
            print("...",count[s[j]])
            maxf = max(maxf, count[s[j]])
            print("Maxf: ",maxf)
            if j - i + 1 > maxf + k:
                count[s[i]] -= 1
                i += 1
        return len(s) - i

solution = Solution()

s = "ABBA"

print(solution.characterReplacement(s,k=2))