from chap3.ex58.functions.Employee import Employee
from chap3.ex58.functions.employeeManagement import employeeManagement

emp1 = Employee('cuc', 'cu', 34)
emp2 = Employee('chim', 'se', 56)

em = employeeManagement()
em.add_employee(emp1)
em.add_employee(emp2)

print('employee list:')
em.print_all()

print('who has more products?')
em.compare()

print('salary of each employee:')
print(f'{emp1.lname} has earned {emp1.get_salary()}')
print(f'{emp2.lname} has earned {emp2.get_salary()}')