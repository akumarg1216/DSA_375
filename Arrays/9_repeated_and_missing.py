class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        result=[]
        max = 0 
        min = 0 
        for i in A:
            if A.count(i) > 1 and i not in result:
                result.append(i)
        A = list(A)
        A.sort()
        max = A[-1]
        min = A[0]
        
        for i in range(1,max):
            if i not in A:
                result.append(i)
        
        return result

A = (2,2)

tuple =Solution()

print(tuple.repeatedNumber(A))

        