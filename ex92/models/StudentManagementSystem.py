import pickle

from chap4.ex92.models.Course import Course
from chap4.ex92.models.Student import Student
from chap4.ex92.models.Subject import Subject


class StudentManagementSystem:
    def __init__(self):
        self.Courses = {}
        self.Students = {}
        self.Subjects = {}
    def add_class(self, CourseID, CourseName):
        self.Courses[CourseID] = Course(CourseID, CourseName)
    def add_student(self, StudentID, StudentName, StudentYearOfBirth, CourseID):
        if CourseID not in self.Courses:
            print(f'CourseID {CourseID} not found')
            return
        student = Student(StudentID, StudentName, StudentYearOfBirth, CourseID)
        self.Students[StudentID] = student
        self.Courses[CourseID].add_student(student)
    def add_subject(self, SubjectID, SubjectName, NumberOfCredits):
        self.Subjects[SubjectID] = Subject( SubjectID,SubjectName, NumberOfCredits)
    def print_courses(self):
        for course in self.Courses.values():
            print(course)
    def print_students(self, CourseID):
        if CourseID in self.Courses:
            for student in self.Courses[CourseID].ListStudents:
                print(student)
        else:
            print(f'CourseID {CourseID} not found')

    def save_data(self, filename = 'student_data.pkl'):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
        print('Data saved')

    @staticmethod
    def load_data(filename="student_data.pkl"):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("File not found!")
            return None