def squirrel_play(temp, is_summer):
  if is_summer == True:
    if temp >= 60 and temp<=100:
      return True
  elif is_summer == False:
    if temp>=60 and temp<=90:
      return True
  return False