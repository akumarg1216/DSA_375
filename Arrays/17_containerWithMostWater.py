class Solution:

    def maxArea(self,height):
        left = 0
        right = len(height)-1
        res = 0
        
        while left < right:
            width = right - left
            min_height = min(height[left],height[right])
            res = max(res,min_height*width)
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1

        return res

solution = Solution()

height = [1,8,6,2,5,4,8,3,7]

print(solution.maxArea(height=height))