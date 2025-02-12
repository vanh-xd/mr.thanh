from chap3.ex63.models.Product import Product


class nonOfficialProduct(Product):
    def get_discount(self):
        return self.price*0.92