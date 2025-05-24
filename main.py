from typing import List

class Solution:
  def calc_maximum_sum(self, nums: List[int]):
    max_current = max_global = nums[0]
    
    for i in range(1, len(nums)):
      max_current = max(nums[i], max_current + nums[i])
      
      if (max_current > max_global):
        max_global = max_current
    
    return max_global
  
nums = [-2,1,-3,4,-1,2,1,-5,4]

sol = Solution()

print(sol.calc_maximum_sum(nums))