class Student:
    def __init__(self, StudentID, StudentName, StudentYearOfBirth, CourseID):
        self.StudentID = StudentID
        self.StudentName = StudentName
        self.StudentYearOfBirth = StudentYearOfBirth
        self.CourseID = CourseID
    def __str__(self):
        return f'{self.StudentID}\t{self.StudentName}\t{self.StudentYearOfBirth}\t{self.CourseID}'