import requests
import re
import getpass

# Ask for login crediantials to user, @ogr.deu.edu.tr is not needed

print("Type without @ogr.deu.edu.tr")
username = input("Username: ")
password = getpass.getpass("Password: ")

print("Select the semester you would like to look.")
print("1- 2017-2018 Fall")
print("2- 2017-2018 Spring")
print("3- 2018-2019 Fall")
print("4- 2018-2019 Spring")

menuChoice = int(input("Menu: "))
if menuChoice == 1:
	semesterID = int(243)
elif menuChoice == 2:
	semesterID = int(244)
elif menuChoice == 3:
	semesterID = int(253)
elif menuChoice == 4:
	semesterID = int(254)

#Post data for debis.deu.edu.tr

payload = {
	"username": username,
    "emailHost": "ogr.deu.edu.tr",
	"password": password,
	"tamam": "Gönder",
	"ogretim_donemi_id": semesterID
}

#Starting session because we will need GET requests later

session_requests = requests.session()
login_url = "http://debis.deu.edu.tr/OgrenciIsleri/Ogrenci/OgrenciNotu/index.php"

result = session_requests.post(
	login_url, 
	data = payload
)
response = result.text

#Find course identities and find exam results accourding to it

courseIdentity = re.findall(r'[A-Z]{1}_[A-Z]{2}\s_[0-9]{1}_\d*_\d*_\d*_', response)

for identity in courseIdentity:
	course = session_requests.post(
		login_url, 
		data = {
    	"ogretim_donemi_id": semesterID,
    	"ders": identity
	}
	)
	courseResult = re.findall(r'<td align=\Wcenter\W>([0-9]{2}|[0-9]{3})<\/td>', course.text)
	courseGrade = re.findall(r'<td align=\Wcenter\W>([A-Z]{2}\s)<\/td>', course.text)
	courseName = re.findall(r'(?<=b>)\w*\s\d*\s-\s([^<]+)', course.text)
	examNumber = len(courseResult)

# Check for Turkish character in the course name, if its True change it.

	if re.search(r'Ý', str(courseName)) is not None:
		courseName = re.sub(r'Ý', r'İ', str(courseName))
		courseName = re.sub(r'ý', r'ı', str(courseName))
		courseName = re.sub(r'\[\'', r'', str(courseName))
		courseName = re.sub(r'\'\]', r'', str(courseName))


	if examNumber > 5:
		print (', '.join(courseName))
		print("Midterm Result: " + courseResult[1])
		print("Final Result: " + courseResult[5])
		print("Additional Result: " + courseResult[3])
		print ("Grade: " + ', '.join(courseGrade))
	elif examNumber > 3:
		if re.search(r'İ', str(courseName)) is not None:
			print(courseName)
			print("Midterm Result: " + courseResult[1])
			print("Final Result: " + courseResult[3])
			print ("Grade: " + ', '.join(courseGrade))
		else:
			print (', '.join(courseName))
			print("Midterm Result: " + courseResult[1])
			print("Final Result: " + courseResult[3])
			print ("Grade: " + ', '.join(courseGrade))
	elif examNumber <= 2:
		print (', '.join(courseName))
		print("Midterm Result: " + courseResult[1])
	else:
		print("Result did not announced yet")
