import time
import re
from decimal import Decimal



midterm = int(input("Midterm Note: "))  # take user input
print("-"*17)
midterm = midterm * 40 / 100
estimated_notes = []
for i in range(50, 101):
    final = i * 60 / 100
    result = midterm + final
    result = round(result, 2)
    result = int(result)
    estimated_notes.append(result)
final_notes = []
n = int(50)
for i in range(len(estimated_notes)):
    final_notes.append(n)
    n = n + 1

grade1 = [i for i in estimated_notes if i >= 90]
grade2 = final_notes[(-len(grade1)):]

if grade1:
    print("AA\nFinal Note: {}\nEstimated Note: {}".format(grade2, grade1))
else:
    print("You can't get AA")

final_notes = final_notes[:len(final_notes)-(len(grade1))]
estimated_notes = estimated_notes[:len(estimated_notes)-(len(grade1))]
print("-"*30)

# update final estimated note lists

def update_final(subtract, final_notes):
    final_notes = final_notes[:len(final_notes)-(len(subtract))]
    return final_notes

def update_estimated(subtract, estimated_notes):
    estimated_notes = estimated_notes[:len(estimated_notes)-(len(subtract))]
    return estimated_notes

# calculation for ba bb cb cc dc dd

def estimated_note(grade1,grade,grade_limit,final_notes, estimated_notes):

    grade3 = [i for i in estimated_notes if i >= grade_limit]
    grade4 = final_notes[(-len(grade3)):]

    if grade3:
        print("{}\nFinal Note: {}\nEstimated Note: {}".format(grade, grade4, grade3))
    else:
        print("You can't get BA")
    return grade3

grade_list = ["BA", "BB", "CB", "CC", "DC", "DD"]
grade_number = [85, 80, 75, 70, 65, 60]

for i in range(len(grade_list)):
    grade3 = estimated_note(grade1, grade_list[i], grade_number[i], final_notes, estimated_notes)
    final_notes = update_final(grade3, final_notes)
    estimated_notes = update_estimated(grade3, estimated_notes)
    print("-"*50)
