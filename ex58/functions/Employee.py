class Employee:
    def __init__(self,  lname, fname, product_quantity_of_each):
        self._lname = lname
        self._fname = fname
        self._productQuantityOfEach = max(0, product_quantity_of_each)
    def __str__(self):
        infor = f'{self.lname}\t{self.fname}\t{self.product_quantity_of_each}'
        return infor
    def get_salary(self):
        if 1 <= self.product_quantity_of_each <= 199:
            return self.product_quantity_of_each*0.5
        elif 200 <= self.product_quantity_of_each <= 399:
            return self.product_quantity_of_each*0.55
        elif 400 <= self.product_quantity_of_each <= 599:
            return self.product_quantity_of_each*0.6
        elif self.product_quantity_of_each >= 600:
            return self.product_quantity_of_each*0.65
        else:
            return 0
    def get_lname(self):
        return self.lname
    def set_lname(self, lname):
        self.lname = lname
    def get_fname(self):
        return self.fname
    def set_fname(self, fname):
        self.fname = fname
    def get_productQuantityOfEach(self):
        return self.product_quantity_of_each
    def set_productQuantityOfEach(self, product_quantity_of_each):
        if self.product_quantity_of_each < 0:
            self.product_quantity_of_each = 0
        else:
            self.product_quantity_of_each = product_quantity_of_each
    lname = property(get_lname, set_lname, 'lname')
    fname = property(get_fname, set_fname, 'fname')
    product_quantity_of_each = property(get_productQuantityOfEach, set_productQuantityOfEach, 'product_quantity_of_each')
    def isHigher(self, emp2):
        return self.product_quantity_of_each > emp2.product_quantity_of_each
