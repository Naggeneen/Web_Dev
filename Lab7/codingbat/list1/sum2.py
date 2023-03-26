def sum2(nums):
  length = len(nums)
  if length == 1:
    sum = nums[0]
  elif length == 0:
    sum = 0
  else:
    sum = nums[0] + nums[1]
  return sum