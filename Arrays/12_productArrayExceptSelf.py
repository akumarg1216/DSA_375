class Solution:
    def productExceptSelf(self, nums):
        numsLen = len(nums)
        productWithoutSelf = [1] * numsLen
        
        # productWithoutSelf[i] as product of elements to the left of nums[i].
        for i in range(1, numsLen):
            productWithoutSelf[i] = productWithoutSelf[i - 1] * nums[i - 1]
            #print(productWithoutSelf)
        
        # productWithoutSelf[i] multiply product of elements to the right of nums[i].
        rightProduct = 1
        for i in range(numsLen - 1, -1, -1):
            print("i= ",i)
            productWithoutSelf[i] *= rightProduct
            print(productWithoutSelf)
            rightProduct = rightProduct * nums[i]
            print("Right Product: ",rightProduct)
            print("=========================================")
            
        return productWithoutSelf

nums = [1,2,3,4]

solution = Solution()

print(solution.productExceptSelf(nums))