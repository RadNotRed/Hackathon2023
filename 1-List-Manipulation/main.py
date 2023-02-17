import random


# Apollo 14
def removeDuplicates(listA):  # removes duplicates in the list
    count = -1
    countB = 0
    while (count < len(listA)):
        while (countB < len(listA)):
            if (listA[count] == listA[countB] and count != countB):
                listA.remove(listA[countB])
            countB += 1
        count += 1


def order(listA):  # orders the list
    counter = 0
    while counter < 50:
        lowest = 101
        countC = 0
        while (countC < len(listA)):
            if (listA[countC] < lowest):
                lowest = listA[countC]
                listB.append(listA[countC])
            countC += 1


listA = []
listB = []

limiter = 0
min = 101

while limiter < 50:
    listA.append(random.randint(1, 100))
    if listA[limiter] < min:
        min = listA[limiter]
    limiter += 1

print("unsorted list: " + str(listA))
print("minimum: " + str(min))

removeDuplicates(listA)
print("list without dups" + str(listA))
