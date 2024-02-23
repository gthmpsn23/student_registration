# student_reg.py
# Function that validates users age

import sqlite3

connection = sqlite3.connect("test.db")

def get_valid_age():
    while True:
        age_input = input("Enter the student's age: ")
        try:
            age = int(age_input)
            if 18 <= age <= 100:
                return age
            else:
                print("Age must be between 18 and 100.")
        except ValueError:
            print("Invalid age. Please enter a number.")

# Person class

class Person:
    def __init__(self, name: str, age: int, ):
        self.name = name
        self.age = age

# student class

class Student(Person):
    def __init__(self, name: str, age: int, subject: str):
        super().__init__(name, age,)
        self.subject = subject

# Course class, holds list where students are stored

class Course():
    def __init__(self, subject):
        self.subject = subject
        self.enrolled_students = []

# Enroll function, adds students to list

    def enroll(self, student):
        self.enrolled_students.append(student)

# function that prints enrolled students name age and subject

    def print_enrolled_students(self):
        for student in self.enrolled_students:
            print(f"{student.name}, age: {student.age}, subject: {student.subject}")

# course list

courses = [Course("Computer Science"), Course("English Literature"), Course("Spanish"), 
               Course("Physics"), Course("History"), Course("Sociology"), 
               Course("Chemistry"), Course("French")]   

#  create students function, holds lists for courses and allows user to add new students

def create_student():
    while True:
        name = input("Please enter the students name: ")
        age = get_valid_age()
        print("\n--- Available Courses ---\n")
        for index, course in enumerate(courses, start=1):
            print(f"{index}: {course.subject}")
        while True:
            try:
                selection = int(input("\nPlease select the subject you want to apply for: "))
                if 1 <= selection <= len(courses):
                    selected_course = courses[selection - 1]
                    print(f"{name} enrolled in {selected_course.subject}")
                    break
                else:
                    print("Invalid task number. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
        new_student = Student(name, age, selected_course.subject)
        selected_course.enroll(new_student)  # Enroll the student in the selected course
       
        add_another = input("Do you want to add another student? (y/n): ")
        if add_another != "y":
            break


# new_student, selected_course = create_student()
# print(f"Added new student: {new_student.name}, age: {new_student.age}, subject: {new_student.subject}")
# selected_course.print_enrolled_students()

# def print_courses(courses):
#     print("\n--- Available Courses ---\n")
#     for index, course in enumerate(courses, start=1):
#         print(f"{index} {course.subject}")

def main_menu():
        print("\n--- Welcome to the student registration system ---\n")
        print("--- Main Menu ---\n")
        print("1. Add Student\t2. View Enrolled Students\t3. Exit Program")
        while True:
            menu = input("Please choose an option: ")
            if menu == "1":
                create_student()
            elif menu == "2":
                 print("Attempting to view enrolled students...")
            elif menu == "3":
                print("Exiting")
                break
            else: 
                print("Incorrect input, try again")
                

main_menu()













