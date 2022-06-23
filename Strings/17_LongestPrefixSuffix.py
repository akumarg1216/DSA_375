class Solution:

    def lps(self,s):

        n = len(s)
        k,j = 0,1
        
        while (j+k) < n:
            if s[k] == s[j+k]:
                k += 1
            
            elif s[k] != s[j+k]:
                j+= 1
                k = 0
        
        return k

solution = Solution()
s = "ababab"

print(solution.lps(s))

