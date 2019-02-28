import time
import re
from decimal import Decimal

midterm = int(input("Midterm: "))
midterm = midterm * 40 / 100
list = []
for i in range(50, 101):
    final = i * 60 / 100
    result = midterm + final
    result = round(result, 2)
    result = int(result)
    list.append(result)

n = int(50)
print("Final Note    Estimated Note")
print("----------    --------------")
for i in range(len(list)):
    print(str(n) + "                  " + str(list[i]))
    n = n + 1

# Divide the list between odds and evens (final note and estimated note)

#finalNote = list[0:][::2]
#estimatedNote = list[1:][::2]


#j2 = [i for i in estimatedNote if i >= 90]

#print(j2)

#for i in range(len(j2)):
#    print(finalNote[-i])
