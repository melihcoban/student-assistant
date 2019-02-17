import sqlite3

class AttendanceDatabase(object):
    # Create database in project folder + create database table
    def __init__(self, filename='attendance.db'):
        self.databasefilename = filename
        db = sqlite3.connect('attendance.db')
        c = db.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS attendanceTrack\
        (id INTEGER PRIMARY KEY, coursename TEXT, current INTEGER, max INTEGER)")
        db.commit()
        c.close()
    # Add new entry to database
    def dynamic_data_entry():
        #date = datetime.date.today()
        db = sqlite3.connect('attendance.db')
        c = db.cursor()
        c.execute("INSERT or IGNORE INTO attendanceTrack (id, coursename, current, max) VALUES (null, ?, ?, ?)",
        (coursename, current, max))
        db.commit()
        c.close()
    # Erase entry from database
    def data_erase():
        db = sqlite3.connect('attendance.db')
        c = db.cursor()
        c.execute("DELETE FROM attendanceTrack WHERE date=?", (deleteData,))
    ## PLANNED : Update entry from database
    def data_update():
        db = sqlite3.connect('attendance.db')
        c = db.cursor()
        c.execute("UPDATE attendanceTrack SET current=? WHERE coursename=?", (newCurrent, coursename))
        db.commit()
        c.close()
    # List all entries
    def data_list_all():
        db = sqlite3.connect('attendance.db')
        c = db.cursor()
        c.execute("SELECT * FROM attendanceTrack")
        rows = c.fetchall()
        for row in rows:
            print(row)

# Create database + table

AttendanceDatabase()

# Menu

print("1: Add New Entries")
print("2: Update Entries")
print("3: Delete Entries")
print("4: Show Entries")
menu = int(input("Menu: "))

if menu == 1:
    courseNumber = int(input("How many courses?: "))
    for i in range(courseNumber):
        coursename = input("Name: ")
        current = input("Current: ")
        max = input("Max: ")
        AttendanceDatabase.dynamic_data_entry()
if menu == 2:
    updateNum = int(input("How many courses you would like to update?: "))
    for i in range(updateNum):
        coursename = input("Course Name: ")
        newCurrent = input("Current Attendance: ")
        AttendanceDatabase.data_update()
    print("Database updated successfully!")
if menu == 3:
    Print("TODO")
if menu == 4:
    AttendanceDatabase.data_list_all()
