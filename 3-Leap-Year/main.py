#Apollo 14

leap = False
year = input("Please enter the year")

if (year % 4 == 0):
  if (year % 100):
    if(year % 400):
      leap = True
    else:
      leap = False
  else:
    leap = True
else:
  leap = False

print(leap)