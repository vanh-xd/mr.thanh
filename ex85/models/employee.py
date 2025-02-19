class Employee:
    def __init__(self, employeeID, employeeName, userName, password):
        self.employeeID = employeeID
        self.employeeName = employeeName
        self.userName = userName
        self.password = password
    def __str__(self):
        return f'{self.employeeID}\t{self.employeeName}'