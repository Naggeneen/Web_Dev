def common_end(a, b):
  a_first = a[0]
  b_first = b[0]
  a_last = a[len(a)-1]
  b_last = b[len(b)-1]
  if a_first == b_first or a_last == b_last:
    return True
  return False