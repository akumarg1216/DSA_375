class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        arr.sort()
        return arr[k-1]

solution = Solution()
nums = [7, 3, 4, 10, 20, 15]
print(solution.kthSmallest(nums,l=0,r=len(nums)-1,k=int(input("Target Smallest: "))))