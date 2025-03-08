class Subject:
    def __init__(self, SubjectID, SubjectName, NumberOfCredits):
        self.SubjectID = SubjectID
        self.SubjectName = SubjectName
        self.NumberOfCredits = NumberOfCredits
    def __str__(self):
        return f'{self.SubjectID}\t{self.SubjectName}\t{self.NumberOfCredits}'