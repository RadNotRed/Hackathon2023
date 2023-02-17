# Apollo 14
Names = []
Grades = []

count = input("How many grades do you wish to add? ")
limiter = 0

while (limiter < int(count)):
    Names.append(input("Please provide a students name: "))
    Grades.append(int(input("Please enter the corresponding students grade: ")))
    limiter += 1

lowA = 0
lowB = 0

countN = 0
countZ = 0
countA = 0

while (countN < len(Names)):
    if (lowA > Grades[countN]):
        lowB = lowA
        lowA = Grades[countN]
        countZ = countN
    elif (lowB > Grades[countN]):
        lowB = Grades[countN]
        countA = countN
    countN += 1
print("Lowest grade: " + str(Names[countZ]))
print("2nd lowest grade: " + str(Names[countA]))
