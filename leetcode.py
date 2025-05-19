from typing import List

class Solution:
  def pivotIndex(self,nums: List[int]) -> int:
    """Returns the Pivot Index of a given list of numbers.

    Args:
    -----
    nums (int): List of integers

    Returns:
    --------
    int: leftmost pivot index. -1 if such index does not exist
    
    """
    right_sum = sum(nums)
    left_sum = 0
    for ind, number in enumerate(nums):
      # right_sum -= number
      
      if left_sum == right_sum - number - left_sum:
        return ind
      
      left_sum += number

if __name__ == "__main__":
  result = Solution()
  print(result.pivotIndex([1,7,3,6,5,6]))