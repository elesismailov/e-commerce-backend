
from api.models import Customer, Category, Brand, Product

c = Category.objects.first()
b = Brand.objects.first()

for i in range(100):
    p = Product(
            name='Air' + str(i),
            description='A new way to populate!',
            slug='nike-air ' + str(i),
            brand=b,
            category=c,
            in_stock_amount=i,
            sold_amount=0,
            price=i*10,
            )
    p.save()
