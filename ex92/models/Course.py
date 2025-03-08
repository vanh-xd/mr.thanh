class Course:
    def __init__(self, CourseID, CourseName):
        self.CourseID = CourseID
        self.CourseName = CourseName
        self.ListStudents = []
    def __str__(self):
        return f'{self.CourseID}\t{self.CourseName}\t{self.ListStudents}'
    def add_student(self, student):
        self.ListStudents.append(student)
    def remove_student(self, StudentID):
        for student in self.ListStudents:
            if student.StudentID == StudentID:
                self.ListStudents.remove(student)