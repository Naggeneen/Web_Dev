def front_times(str, n):
  front_len = 3

  if len(str)<3:
    front_len = len(str)

  front = str[:front_len]
  result = ""
  
  for i in range(n):
    result = result + front
  return result