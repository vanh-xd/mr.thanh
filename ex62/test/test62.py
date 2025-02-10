from chap3.ex62.models.category import Category
from chap3.ex62.models.product import Product

list = []
c1 = Category('c1', 'thuoc')
c2 = Category('c2', 'nuoc ngot')
c3 = Category('c3', 'bia')
list.extend([c1,c2,c3])
print('danh sach danh muc cua cua hang:')
for c in list:
    print(c)
c1.add_product(Product('p1', 'thuoc tri ghe', 15, 'trung quoc'))
c1.add_product(Product('p2', 'thuoc tri font bart', 20, 'hong kong'))
c2.add_product(Product('p3', 'nuoc khoang', 22, 'vietnam'))
c2.add_product(Product('p4', 'nuoc lon', 12, 'vietnam'))
c2.add_product(Product('p5', 'nuoc dua', 23, 'vietnam'))
c3.add_product(Product('p6', 'bia', 10, 'trung quoc'))

print('danh sach san pham phan loai theo danh muc:')
for c in list:
    print('*'*30)
    print(c)
    print('*'*30)
    for p in c.list_products:
        print(p)

print('-'*30)
c2.del_products('p4')
print('-'*30)

c2.update_products('p3', 'sting chuoi')
print('ds san pham sau khi cap nhat:')
for c in list:
    print('*'*30)
    print(c)
    print('*'*30)
    c.print_products()

print('-'*30)
c1.total_value('p2')
print('-'*30)

c3.country('thai len')