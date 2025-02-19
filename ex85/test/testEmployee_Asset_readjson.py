from chap4.ex85.libs.JsonFileFactory import JsonFileFactory
from chap4.ex85.models.employee_asset import Employee_Asset
from chap4.ex85.test.testEmployee_Asset_writejson import employees_assets

filename = 'employees_assets.json'
path = f'../dataset/{filename}'
jff = JsonFileFactory()
employees = jff.read_data(path, Employee_Asset)
print('list emp_a after readjson:')
for ae in employees_assets:
    print(ae)