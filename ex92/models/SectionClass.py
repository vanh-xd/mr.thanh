class SectionClass:
    def __init__(self, SubjectClassID, SubjectID, NumberOfCredits, StartDate, EndDate):
        self.SubjectClassID = SubjectClassID
        self.SubjectID = SubjectID
        self.NumberOfCredits = NumberOfCredits
        self.StartDate = StartDate
        self.EndDate = EndDate
    def __str__(self):
        return f'{self.SubjectClassID}\t{self.SubjectID}\t{self.NumberOfCredits}\t{self.StartDate}\t{self.EndDate}'