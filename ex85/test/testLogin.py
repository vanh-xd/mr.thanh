from chap4.ex85.libs.DataConnector import DataConnector

uid = 'john'
pwd = '123'
dc = DataConnector()
emp = dc.login(uid, pwd)
if emp == None:
    print('login failed')
else:
    print('login successfully')