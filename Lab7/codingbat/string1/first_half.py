def first_half(str):
  half = len(str)/2
  result=""
  for i in range(half):
    result += str[i]
  return result