#!/usr/bin/env python3

import os
import pickle
from collections import namedtuple

def save_object(filename, obj):
    with open(filename, "wb") as output:
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)

def open_object(filename):
    with open(filename, "rb") as f:
        courses = pickle.load(f)
        return courses

class Course:
    # Total attendance limit for all the courses
    total = 12
    def __init__(self, name, current):
        self.name = name
        self.current = current

    def __str__(self):
        return "Course: {:<10s}\nAttendance: {}".format(self.name, self.current)

    def not_attended(self):
        self.current +=3

    def attendance_left(self):
        self.total -= self.current

courses = []

def new_course():
    name = input("Course Name: ")
    current = int(input("Current Attendance: "))
    card = namedtuple("Course", "name current")
    i = Course(name, current)
    courses.append(i)

# Parse objects
try:
    courses = open_object("courses.pkl")
except:
    print(" ")

# Main
while True:
    print(
"""Attendance Tracking Program v0.1
Welcome Melih, what would you like to do?
1- Add New Course
2- Delete Existing Course
3- Update Course Attendance
4- Attendance List
5- Exit"""
)
    print("-"*20)
    menu = int(input("Menu: "))
    print("-"*20)

    if menu==1:
        new_course()
    elif menu==2:
        select = int(input("Course ID: "))
        courses.pop(select)
    elif menu==3:
        select = int(input("Course ID: "))
        courses[select].not_attended()
        print("Updated successfuly!")
    elif menu==4:
        os.system('clear')
        for i in range(len(courses)):
            print("Index: " + str(i))
            print(courses[i])
            print("-"*30)
    elif menu==5:
        break

    print("-"*20)

# Save objects
try:
    save_object("courses.pkl", courses)
except:
    print(" ")
