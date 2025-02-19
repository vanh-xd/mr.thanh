from chap4.ex85.libs.JsonFileFactory import JsonFileFactory
from chap4.ex85.models.employee import Employee

filename = 'employees.json'
path = f'../dataset/{filename}'
jff = JsonFileFactory()
employees = jff.read_data(path, Employee)
print('list emp after readjson:')
for e in employees:
    print(e)