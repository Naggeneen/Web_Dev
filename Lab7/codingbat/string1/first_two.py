def first_two(str):
  first2 = 2
  if first2 > len(str):
    first2 = len(str)
  return str[:first2]