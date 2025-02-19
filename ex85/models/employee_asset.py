class Employee_Asset:
    def __init__(self, employeeID, assetID, role):
        self.employeeID = employeeID
        self.assetID = assetID
        self.role = role
    def __str__(self):
        return f'{self.employeeID}\t{self.assetID}\t{self.role}'