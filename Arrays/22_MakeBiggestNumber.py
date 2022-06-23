import functools

class Solution:
    def comparator(self,s1, s2):
        if int(s1+s2) < int(s2+s1):
            return -1
        if int(s1+s2) > int(s2+s1):
            return 1
        return 0
    
    def largestNumber(self, nums):
        nums = [str(num) for num in nums]
        nums.sort(key=functools.cmp_to_key(self.comparator))
        nums.reverse()
        ans = '0' if nums[0] == '0' else ''.join(nums)
        return ans

solution = Solution()
nums = [3, 30, 34, 5, 9]
print(solution.largestNumber(nums))