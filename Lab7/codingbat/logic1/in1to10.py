def in1to10(n, outside_mode):
  if outside_mode == True:
    if n <= 1 or n>=10:
      return True
  elif outside_mode == False:
    if n>= 1 and n<=10:
      return True
  return False