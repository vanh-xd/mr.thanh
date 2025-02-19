from chap4.ex85.libs.JsonFileFactory import JsonFileFactory
from chap4.ex85.models.employee import Employee

employees = []
employees.append(Employee('e1', 'john', 'john', '123'))
employees.append(Employee('e2', 'tom', 'tom', '456'))
employees.append(Employee('e3', 'peter', 'peter', '789'))
employees.append(Employee('e4', 'cf', 'cf', 'cfsua'))
print('list employees:')
for e in employees:
    print(e)
#write data into json:
filename = 'employees.json'
path = f'../dataset/{filename}'
jff = JsonFileFactory()
jff.write_data(employees, path)