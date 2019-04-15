import requests
import re
import getpass

# Ask for debis login crediantials to user, @ogr.deu.edu.tr is not needed

print("Welcome Melih, ")
print("Type without @ogr.deu.edu.tr")
username = input("Username: ")
password = getpass.getpass("Password: ")
print("Select the semester!\n1- 2017-2018 Fall\n2- 2017-2018 Spring\n3- 2018-2019 Fall\n4- 2018-2019 Spring\n")

menu_choice = int(input("Menu: "))
if menu_choice == 1:
    semester_id = int(243)
elif menu_choice == 2:
    semester_id = int(244)
elif menu_choice == 3:
    semester_id = int(253)
elif menu_choice == 4:
    semester_id = int(254)
print("-"*30)

#Post data for debis.deu.edu.tr

payload = {
	"username": username,
        "emailHost": "ogr.deu.edu.tr",
	"password": password,
	"tamam": "Gönder",
	"ogretim_donemi_id": semester_id
}

#Starting session because we will need GET requests later

session_requests = requests.session()
login_url = "http://debis.deu.edu.tr/OgrenciIsleri/Ogrenci/OgrenciNotu/index.php"

result = session_requests.post(
        login_url, 
	data = payload
)
response = result.text

#Find course identities in the source code and find exam results accourding to it

course_identity = re.findall(r'[A-Z]{1}_[A-Z]{2}\s_[0-9]{1}_\d*_\d*_\d*_', response)
if not course_identity:
    course_identity = re.findall(r'[A-Z]{1}__\d*_\d*_\d*_\d*_', response)


def http_post(course_identity):
    for identity in course_identity:
        course = session_requests.post(
                login_url, 
                data = {
                "ogretim_donemi_id": semester_id,
                "ders": identity
        }
        )
        course_result = re.findall(r'<td align=\Wcenter\W>([0-9]{2}|[0-9]{3})<\/td>', course.text)
        course_grade = re.findall(r'<td align=\Wcenter\W>([A-Z]{2}\s)<\/td>', course.text)
        course_name = re.findall(r'(?<=b>)\w*\s\d*\s-\s([^<]+)', course.text)
        exam_number = len(course_result)

    # Check for Turkish character in the course name, if its True change it.

        if re.search(r'Ý', str(course_name)) is not None:
            course_name = re.sub(r'Ý', r'İ', str(course_name))
            course_name = re.sub(r'ý', r'ı', str(course_name))
            course_name = re.sub(r'\[\'', r'', str(course_name))
            course_name = re.sub(r'\'\]', r'', str(course_name))

        if exam_number > 5:
            print (', '.join(course_name))
            print("Midterm Result: " + course_result[1])
            print("Final Result: " + course_result[5])
            print("Additional Result: " + course_result[3])
            print("Grade: " + ', '.join(course_grade))
            print("-"*20)
        elif exam_number > 3:
            if re.search(r'İ', str(course_name)) is not None:
                print(course_name)
                print("Midterm Result: " + course_result[1])
                print("Final Result: " + course_result[3])
                print ("Grade: " + ', '.join(course_grade))
                print("-"*20)
            else:
                print (', '.join(course_name))
                print("Midterm Result: " + course_result[1])
                print("Final Result: " + course_result[3])
                print ("Grade: " + ', '.join(course_grade))
                print("-"*20)
        elif exam_number <= 2:
            try:
                if re.search(r'İ', str(course_name)) is not None:
                    print(course_name)
                    print("Midterm Result: " + course_result[1])
                    print("-"*30)
                else:
                    print (', '.join(course_name))
                    print("Midterm Result: " + course_result[1])
                    print("-"*30)
            except IndexError:
                print("Midterm Result: N/A")
                print("-"*30)
        else:
            print("Result did not announced yet")


http_post(course_identity)
