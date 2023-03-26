def alarm_clock(day, vacation):
  if vacation == False:
    if day >=1 and day<=5:
      return "7:00"
  if vacation == True:
    if day ==  6 or day == 0:
      return "off"
  return "10:00"