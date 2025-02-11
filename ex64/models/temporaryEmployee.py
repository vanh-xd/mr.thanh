from chap3.ex64.models.employee import Employee


class temmporaryEmployee(Employee):
    def __init__(self, id=None, idcard=None, name=None, birthday=None, workinghour = 0):
        super().__init__(id, idcard, name, birthday)
        self.workinghour = workinghour
    def calc_salary(self):
        return self.workinghour*300000