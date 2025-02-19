from chap4.ex85.libs.JsonFileFactory import JsonFileFactory
from chap4.ex85.models.asset import Asset

assets = []
assets.append(Asset('a1', 'led monitor', 2019, 200))
assets.append(Asset('a2', 'projector', 2024, 20))
assets.append(Asset('a3', 'laptop', 2011, 89))
assets.append(Asset('a4', 'car', 2017, 300))
print('list of assets:')
for a in assets:
    print(a)

filename = 'assets.json'
path = f'../dataset/{filename}'
jff = JsonFileFactory()
jff.write_data(assets, path)