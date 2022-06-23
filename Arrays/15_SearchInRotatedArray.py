class Solution:
   def search(self, nums, target):
        lo, hi = 0, len(nums) - 1
        iter = 0
        while lo <= hi:
            iter+=1
            mid = (lo+hi) // 2
            if nums[mid] == target:
               return mid
            if nums[0] <= target < nums[mid] or target < nums[mid] < nums[0] or nums[mid] < nums[0] <= target:
               hi = mid - 1
            else:
               lo = mid + 1
        return -1

solution = Solution()
nums = [5,10,76,100,2,3,4]
print(solution.search(nums,target=int(input("Target: "))))