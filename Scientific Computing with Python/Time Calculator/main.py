def add_time(start, duration, dayOfWeek=None):

  dayMentioned = False

  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  # hours, minutes = start.split(':')
  addHours, addMinutes = duration.split(':')
  L = start.split(" ")
  hours, minutes = L[0].split(':')

  i = 0

  if(dayOfWeek != None):
    dayMentioned = True
    weekDay = ""
    weekDay = dayOfWeek
    weekDay = weekDay.capitalize()
    while(True):
      if (weekDay == days[i]):
          weekDay = days[i]
          break
      i = i + 1

  hourNow = int(hours) + int(addHours)
  minutesNow = int(minutes) + int(addMinutes)
  if (minutesNow >= 60):
      minutesNow = minutesNow - 60
      hourNow = hourNow + 1

  # print(str(hourNow) + ':' + str(minutesNow))

  def change_time(dayOrNight):

    if (dayOrNight == "PM"):
        dayOrNight = "AM"
        L[1] = dayOrNight
    elif (dayOrNight == "AM"):
        dayOrNight = "PM"
        L[1] = dayOrNight

  daysPassed = 0
  if (L[1] == "AM"):
      needMinusOne = True
  elif(L[1] == "PM"):
      needMinusOne = False

  while (True):

    if(hourNow >= 12 and hourNow - 12 >= 0):
        hourNow = hourNow - 12
        change_time(L[1])

    if (L[1] == "AM" and needMinusOne == False):
        daysPassed = daysPassed + 1
    elif (L[1] == "PM"):
        daysPassed = daysPassed
    elif (L[1] == "AM" and needMinusOne == True):
        daysPassed = daysPassed
    needMinusOne = False

    if (hourNow - 12 < 0):
        break


  twelve = int(hours)
  if(twelve == 12):
      change_time(L[1])
  if(hourNow == 0):
      hourNow = 12

  dayNow = i


  if (dayNow + daysPassed <= 6):
    dayNow = dayNow + daysPassed
  elif(dayNow + daysPassed > 6):
      dayNow = dayNow + daysPassed
      while (True):
          if((dayNow - 7) < 0):
            break
          else:
            dayNow = dayNow - 7

  # daysToSubstract = daysPassed * 7
  # dayNow = (dayNow + daysPassed) - daysToSubstract

  timenow = ""

  if(daysPassed == 0 and minutesNow > 10 and dayMentioned == False):
    timenow = str(hourNow) + ':' + str(minutesNow) + " " + L[1]
  if(daysPassed == 0 and minutesNow < 10 and dayMentioned == False):
    timenow = str(hourNow) + ':' + "0" + str(minutesNow) + " " + L[1]
  if(daysPassed == 1 and minutesNow > 10 and dayMentioned == False):
    timenow = str(hourNow) + ':' + str(minutesNow) + " " + L[1] + " " + "(next day)"
  if(daysPassed == 0 and minutesNow < 10 and dayMentioned == False):
    timenow = str(hourNow) + ':' + "0" + str(minutesNow) + " " + L[1]
  if(daysPassed > 1 and minutesNow < 10 and dayMentioned == False):
    timenow = str(hourNow) + ':' + "0" + str(minutesNow) + " " + L[1] + " " + '(' + str(daysPassed) + " days later)"

  if(daysPassed > 1 and minutesNow > 10 and dayMentioned == False):
    timenow = str(hourNow) + ':' + str(minutesNow) + " " + L[1] + " " + '(' + str(daysPassed) + " days later)"

  if(daysPassed == 0 and minutesNow > 10 and dayMentioned == True):
    timenow = str(hourNow) + ":" + str(minutesNow) + " " + L[1] + ", " + days[dayNow]
  if(daysPassed == 1 and minutesNow > 10 and dayMentioned == True):
    timenow = str(hourNow) + ":" + str(minutesNow) + " " + L[1] + ", " + days[dayNow] + " (next day)"  
  if(daysPassed > 1 and minutesNow < 10 and dayMentioned == True):
    timenow = str(hourNow) + ":" + "0" + str(minutesNow) + " " + L[1] +", " + days[dayNow] + " " + '(' + str(daysPassed) + " days later)"


  if(daysPassed > 1 and minutesNow > 10 and dayMentioned == True):
    timenow = str(hourNow) + ":" + str(minutesNow) + " " + L[1] +", " + days[dayNow] + " " + '(' + str(daysPassed) + " days later)"

  if (daysPassed == 1 and minutesNow < 10 and dayMentioned == True):
    timenow = str(hourNow) + ":" + "0" + str(minutesNow) + " " + L[1] + ", " + days[dayNow] + " (next day)"


  return timenow

print(add_time("11:34 PM", "2835:59", "tuesday"))





