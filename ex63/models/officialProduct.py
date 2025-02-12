from chap3.ex63.models.Product import Product


class officialProduct(Product):
    def pay_tax(self):
        return self.price*1.1