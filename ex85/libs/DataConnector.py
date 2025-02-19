from chap4.ex85.libs.JsonFileFactory import JsonFileFactory
from chap4.ex85.models.employee import Employee
from chap4.ex85.test.testEmployee_readjson import employees


class DataConnector:
    def load_all_employee(self):
        filename = 'employees.json'
        path = f'../dataset/{filename}'
        jff = JsonFileFactory()
        employees = jff.read_data(path, Employee)
        return employees
    def login(self, username, password):
        employees = self.load_all_employee()
        for emp in employees:
            if emp.userName == username and emp.password == password:
                return emp
        return None