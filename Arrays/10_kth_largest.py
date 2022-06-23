class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        output = nums[k-1]
        return output
        
        
        
        