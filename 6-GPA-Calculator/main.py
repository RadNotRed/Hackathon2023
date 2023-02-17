# Define constants for weight percentages
HONORS_WEIGHT = 1.05
AP_WEIGHT = 1.1
#Apollo 14
# Ask user to input grades for 8 classes
grades = []
for i in range(8):
    grade = float(input("Enter the final average grade for your class {}: ".format(i + 1)))
    grades.append(grade)
AP = input("Which class number has AP weighting? ")
Honors = input("Which class number has honors weighting? ")
# Calculate unweighted GPA by dividing sum of grades by number of grades
unweighted_gpa = sum(grades) / len(grades)

# Calculate weighted GPA
weighted_grades = []
weighted_grades.append(grades[int(AP)] * AP_WEIGHT)
weighted_grades.append(grades[int(Honors)] * HONORS_WEIGHT)
"""for grade in grades:
    # When grade is above 90 it is an AP class
    if grade >= 90:
        weighted_grades.append(grade * AP_WEIGHT)
    # When grade is above 80 it is an honors class
    elif grade >= 80:
        weighted_grades.append(grade * HONORS_WEIGHT)
    else:
        # when grade is below 80 it is not weighted
        weighted_grades.append(grade)"""
# Calculate weighted GPA by dividing sum of weighted grades by number of grades
weighted_gpa = sum(weighted_grades) / len(weighted_grades)

# Print GPA calculations
print("Unweighted GPA: {:.2f}".format(unweighted_gpa))
print("Weighted GPA: {:.2f}".format(weighted_gpa))
