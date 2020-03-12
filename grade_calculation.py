# Calculate final result and print according to it

# 

def calculation(midterm, final):
    result = int(midterm) * 40 / 100 + int(final) * 60 / 100
    result = int(result)
    if 90 <= result <= 100:
        grade = "AA"
    elif 85 <= result <= 90:
        grade = "BA"
    elif 80 <= result <= 85:
        grade = "BB"
    elif 75 <= result <= 80:
        grade = "CB"
    elif 70 <= result <= 75:
        grade = "CC"
    elif 65 <= result <= 70:
        grade = "DC"
    elif 60 <= result <= 65:
        grade = "DD"
    elif 50 <= result <= 60:
        grade = "FD"
    elif 0 <= result <= 50:
        grade = "FF"
#    print("Average: " + str(result))
#    print("Grade: " + str(grade))
#    print("------------")
    result = ("Average: {}\nGrade: {}".format(result, grade))
    print(result)
    return result

# Ask user to how many times they would like to calculate

repeatNumber = int(input("How many courses you would like to calculate?: "))
for i in range(repeatNumber):
    midterm = int(input("Midterm: "))
    final = int(input("Final: "))
    calculation(midterm, final)
