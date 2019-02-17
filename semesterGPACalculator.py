# Modules

from decimal import Decimal
import numpy as np

# Define functions

def readyAverage(C1, C2, C3, C4, C5, C6, C7):
    creditSum = 3 * C1 + 3 * C2 + 3 * C3 + 3 * C4 + 3 * C5 + 3 * C6 + 2 * C7
    result = creditSum / 20
    result = Decimal(result)
    result = round(result, 2)
    print("GPA: " + str(result))

def customAverage(creditList, gradeList):
    creditSum = np.multiply(creditList,gradeList)
    creditSum = sum(creditSum)
    totalCredit = sum(creditList)
    result = creditSum / totalCredit
    result = round(result, 2)
    print("GPA: " + str(result))

# Ask user for custom input or pre-prepared one

print("Semester Average Calculation (GPA)")
print("1- Ready Mode (7 Courses)")
print("2- Custom Mode")
choice = int(input("Menu: "))

if choice == 1:
    print("Numbers equivalent to grades")
    print("AA: 4.0, BA: 3.50, BB: 3.0, CB: 2.50, CC: 2.00, DC: 1.50, DD: 1.00, FD: 0.50, FF: 0.0")
    try:
        C1 = float(input("1: "))
        C2 = float(input("2: "))
        C3 = float(input("3: "))
        C4 = float(input("4: "))
        C5 = float(input("5: "))
        C6 = float(input("6: "))
        C7 = float(input("7: "))
        readyAverage(C1, C2, C3, C4, C5, C6, C7)
    except ValueError:
        print("Please enter the correct number")
elif choice == 2:
    gradeNumber = 1
    creditNumber = 1
    creditList = []
    courseNumber = int(input("Course Number: "))
    print("Please enter course credits")
    for i in range(courseNumber):
        courseCredit = int(input(str(creditNumber) + ": "))
        creditList.append(courseCredit)
        creditNumber = creditNumber + 1
    print("----------------------------")
    print("Numbers equivalent to grades")
    print("AA: 4.0, BA: 3.50, BB: 3.0, CB: 2.50, CC: 2.00, DC: 1.50, DD: 1.00, FD: 0.50, FF: 0.0")
    gradeList = []
    for i in range(courseNumber):
        courseGrade  = float(input(str(gradeNumber) + ": "))
        gradeList.append(courseGrade)
        gradeNumber = gradeNumber + 1
    customAverage(creditList,gradeList)
