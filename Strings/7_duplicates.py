class Solution:

    def allDuplicates(self,s):
        dict = {}

        for i in s:
            if s.count(i)>1 and i!= " ":
                dict[i] = s.count(i)

        print(dict)

        for keys in dict:
            print(f"{keys}, count = {dict.get(keys)}")

        

duplicates = Solution()
s = "test string it is"
duplicates.allDuplicates(s)