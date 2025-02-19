class employeeManagement:
    def __init__(self):
        self.database = []
    def add_employee(self, emp):
        self.database.append(emp)
    def print_all(self):
        for emp in self.database:
            print(emp)
    def compare(self):
        if len(self.database) < 2:
            print('add 1 more employee')
            return

        if self.database[0].isHigher(self.database[1]):
            print(f'employee {self.database[0].lname} has more products')
        else:
            print(f'employee {self.database[1].lname} has more products')

        if self.database[0].product_quantity_of_each > self.database[1].product_quantity_of_each:
            print(f'employee {self.database[0].lname} has more products')
        elif self.database[0].product_quantity_of_each < self.database[1].product_quantity_of_each:
            print(f'employee {self.database[1].lname} has more products')
        else:
            print(f'2 employees have the same number of products')