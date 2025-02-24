class Product:
    def __init__(self, ProductID, ProductName, Price):
        self.ProductID =ProductID
        self.ProductName = ProductName
        self.Price = Price
    def __str__(self):
        return str(self.ProductID)+' - '+self.ProductName+' - '+str(self.Price)