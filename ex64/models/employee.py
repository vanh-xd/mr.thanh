class Employee:
    def __init__(self, id = None, idcard = None, name = None, birthday = None):
        self.id = id
        self.idcard = idcard
        self.name = name
        self.birthday = birthday
    def calc_salary(self):
        return 20000000