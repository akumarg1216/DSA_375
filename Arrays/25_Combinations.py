class Solution:
    def combine(self, n: int, k: int):
        combs = [[]]
        
        for _ in range(k):
            print("Combs: ",combs)
            print("_= ",_)
            temp = []
            for c in combs:
                print("C= ",c)
                for i in range(1, c[0] if c else n+1):
                    temp.append([i]+c)
                    print("Temp: ",temp)
            combs = temp
            print("*****************************************")
        return combs

solution = Solution()
n = 5
k = 3
print(solution.combine(n,k))