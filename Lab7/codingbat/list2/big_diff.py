def big_diff(nums):
  min_v = 1e9
  max_v =0
  for i in range(len(nums)):
    if nums[i] > max_v:
      max_v = nums[i]
    if nums[i] < min_v:
      min_v = nums[i]
  return max_v - min_v