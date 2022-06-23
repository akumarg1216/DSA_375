class Solution:
    
    def removeCons(self,s):
        new_s = ""
        prev = ""
        for c in s:
            if len(new_s) == 0:
                new_s += c
                prev = c
            if c == prev:
                continue
            else:
                new_s += c
                prev = c
        return new_s

solution = Solution()

s = "aabb"

print(solution.removeCons(s))