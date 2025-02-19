from chap4.ex85.libs.JsonFileFactory import JsonFileFactory
from chap4.ex85.models.employee_asset import Employee_Asset

employees_assets = []
employees_assets.append(Employee_Asset('e1', 'as1', 'main'))
employees_assets.append(Employee_Asset('e2', 'as2', 'main'))
employees_assets.append(Employee_Asset('e3', 'as3', 'main'))
employees_assets.append(Employee_Asset('e4', 'as4', 'main'))
print('list employees - assets:')
for ea in employees_assets:
    print(ea)

filename = 'employees_assets.json'
path = f'../dataset/{filename}'
jff = JsonFileFactory()
jff.write_data(employees_assets, path)