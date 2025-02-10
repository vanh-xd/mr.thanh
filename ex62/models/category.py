class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.list_products = []  #1 danh muc co nhieu sp
    def __str__(self):
        return f'{self.id}\t{self.name}'
    def add_product(self, p):
        self.list_products.append(p)
    def print_products(self):
        for p in self.list_products:
            print(p)  #xuat sp theo danh muc
    def del_products(self, product_id):
        for product in self.list_products:
            if product.id == product_id:
                print(f'product with id = {product_id} has just been deleted')
                self.list_products.remove(product)
                return
    def update_products(self, product_id, name = None, price = None, madein = None):
        for x in self.list_products:
            if x.id == product_id:
                if name is not None:  #them None vao thi khi goi def update_products, kh can nhap value vao neu inst do khong thay doi
                    x.name = name
                if price is not None:
                    x.price = price
                if madein is not None:
                    x.madein = madein
                print(f'product with id = {x.id} has just been updated')
                return
    def total_value(self, product_id):
        for x in self.list_products:
            if x.id == product_id:
                total = x.price
                print(f'item {x.name} has total value of {total}')
                return total
    def country(self, origin):
        turnout = False
        for x in self.list_products:
            if x.madein.lower().strip() == origin.lower().strip():
                print(f'product {x.name} from {origin}')
                turnout = True
        if not turnout:
            print(f'no products from {origin}')