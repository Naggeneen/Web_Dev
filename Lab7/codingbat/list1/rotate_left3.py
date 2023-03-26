def rotate_left3(nums):
  for i in range(1):   
    first = nums[0];    
        
    for j in range(0, len(nums)-1):
        nums[j] = nums[j+1];    
            
    nums[len(nums)-1] = first;
    return nums