import time
import re
from decimal import Decimal

midterm = int(input("Midterm Note: "))
print("-"*17)
midterm = midterm * 40 / 100
estimatedNote = []
for i in range(50, 101):
    final = i * 60 / 100
    result = midterm + final
    result = round(result, 2)
    result = int(result)
    estimatedNote.append(result)
finalNote = []
n = int(50)
for i in range(len(estimatedNote)):
#    print(str(n) + "                  " + str(estimatedNote[i]))
    finalNote.append(n)
    n = n + 1
#    time.sleep(0.05)

# Divide the estimatedNote between odds and evens (finalNote note and estimated note)
#finalNoteNote = estimatedNote[0:][::2]
#estimatedNote = estimatedNote[1:][::2]


# Calculate AA

aa1 = [i for i in estimatedNote if i >= 90]
#aa2 = [i for i in finalNote if i >= 90]
aa3 = finalNote[(-len(aa1)):]

if aa1:
    print("AA: Final Note: " + str(aa3) + " Estimated Note: " + str(aa1))
else:
    print("You can't get AA")

# Calculate BA

estimatedNote = estimatedNote[:len(estimatedNote)-(len(aa1))]
finalNote = finalNote[:len(finalNote)-(len(aa1))]

ba1 = [i for i in estimatedNote if i >= 85]
#ba2 = [i for i in finalNote if i >= 85]
ba3 = finalNote[(-len(ba1)):]

if ba1:
    print("BA: Final Note: " + str(ba3) + " Estimated Note: " + str(ba1))
else:
    print("You can't get BA")


# Calculate BB

estimatedNote = estimatedNote[:len(estimatedNote)-(len(ba1))]
finalNote = finalNote[:len(finalNote)-(len(ba1))]

bb1 = [i for i in estimatedNote if i >= 80]
#bb2 = [i for i in finalNote if i >= 80]
bb3 = finalNote[(-len(bb1)):]

if bb1:
    print("BB: Final Note: " + str(bb3) + " Estimated Note: " + str(bb1))
else:
    print("You can't get BB")


# Calculate CB

estimatedNote = estimatedNote[:len(estimatedNote)-(len(bb1))]
finalNote = finalNote[:len(finalNote)-(len(bb1))]

cb1 = [i for i in estimatedNote if i >= 75]
#cb2 = [i for i in finalNote if i >= 75]
cb3 = finalNote[(-len(cb1)):]

if cb1:
    print("CB: Final Note: " + str(cb3) + " Estimated Note: " + str(cb1))
else:
    print("You can't get CB")


# Calculate CC

estimatedNote = estimatedNote[:len(estimatedNote)-(len(cb1))]
finalNote = finalNote[:len(finalNote)-(len(cb1))]

cc1 = [i for i in estimatedNote if i >= 70]
#cc2 = [i for i in finalNote if i >= 70]
cc3 = finalNote[(-len(cc1)):]

if cc1:
    print("CC: Final Note: " + str(cc3) + " Estimated Note: " + str(cc1))
else:
    print("You can't get CC")


# Calculate DC

estimatedNote = estimatedNote[:len(estimatedNote)-(len(cc1))]
finalNote = finalNote[:len(finalNote)-(len(cc1))]

dc1 = [i for i in estimatedNote if i >= 65]
#dc2 = [i for i in finalNote if i >= 65]
dc3 = finalNote[(-len(dc1)):]

if dc1:
    print("DC: Final Note: " + str(dc3) + " Estimated Note: " + str(dc1))
else:
    print("You can't get DC")


# Calculate DD

estimatedNote = estimatedNote[:len(estimatedNote)-(len(dc1))]
finalNote = finalNote[:len(finalNote)-(len(dc1))]

dd1 = [i for i in estimatedNote if i >= 60]
#dd2 = [i for i in finalNote if i >= 60]
dd3 = finalNote[(-len(dd1)):]

if dd1:
    print("DD: Final Note: " + str(dd3) + " Estimated Note: " + str(dd1))
else:
    print("You can't get DD")
