import time
import re
from decimal import Decimal

# Update both final note and estimated note list after calculating every
# grade such as BA, BB, CB, CC, DC, DD
def update_final(subtract, final_notes):
    final_notes = final_notes[:len(final_notes)-(len(subtract))]
    return final_notes

def update_estimated(subtract, estimated_notes):
    estimated_notes = estimated_notes[:len(estimated_notes)-(len(subtract))]
    return estimated_notes

# Calculates every final and estimated note according to grade limit
# and then substracts the values from the lists
def calculate_notes(grade,grade_limit,final_notes, estimated_notes):
    estimated_note = [i for i in estimated_notes if i >= grade_limit] # Grade limit ex AA = 90
    final_note = final_notes[(-len(estimated_note)):]

    if estimated_note:
        print("{}\nFinal Note: {}\nEstimated Note: {}".format(grade, final_note, estimated_note))
    else:
        print("You can't get BA")

    return estimated_note

midterm = int(input("Midterm Note: ")) 
print("-"*17)
midterm = midterm * 40 / 100
estimated_notes = []

for i in range(50, 101):
    # Create a final note between 50-100 and add it to the list and then
    # sum up midterm note with final note and round it
    final = i * 60 / 100
    result = midterm + final
    result = round(result, 2)
    result = int(result)
    estimated_notes.append(result)

final_notes = []
n = int(50)

for i in range(len(estimated_notes)):
    # Append all of the available final notes to the list according to
    # the estimated note
    final_notes.append(n)
    n = n + 1

# Look for the AA grade in the estimated notes and delete the equivalent final
# note from the final_notes list
estimated_note = [i for i in estimated_notes if i >= 90]
final_note = final_notes[(-len(estimated_note)):]

if estimated_note:
    print("AA\nFinal Note: {}\nEstimated Note: {}".format(final_note, estimated_note))
else:
    print("You can't get AA")

final_notes = final_notes[:len(final_notes)-(len(estimated_note))]
estimated_notes = estimated_notes[:len(estimated_notes)-(len(estimated_note))]
print("-"*30)

grade_list = ["BA", "BB", "CB", "CC", "DC", "DD"]
grade_number = [85, 80, 75, 70, 65, 60]

# Loops through every grade and updates the final and estimated notes lists
for i in range(len(grade_list)):
    estimated_note = calculate_notes(grade_list[i], grade_number[i], final_notes, estimated_notes)
    final_notes = update_final(estimated_note, final_notes)
    estimated_notes = update_estimated(estimated_note, estimated_notes)
    print("-"*50)
