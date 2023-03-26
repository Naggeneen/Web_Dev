def count_hi(str):
  result = 0
  for i in range(len(str)-1):
    if str[i] == "h" and str[i+1] == "i":
      result += 1
  return result