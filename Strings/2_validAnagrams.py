s="anagram"
t="naragam"

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list=[]
        for i in range(97,123):
            list.append(chr(i))
        return all(s.count(x) == t.count(x) for x in list)

solution = Solution()
print(solution.isAnagram(s,t))
   