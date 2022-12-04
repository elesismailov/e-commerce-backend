
from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class Product(models.Model):

    name            = models.CharField(max_length=50)
    description     = models.CharField(max_length=250)
    
    slug            = models.CharField(max_length=50)

    # TODO how to change category if the category/brand was deleted
    #   (on_delete='do something with the category')
    category        = models.ForeignKey(Category)
    brand           = models.ForeignKey(Brand)

    in_stock_amount = models.IntegerField()
    sold_amount     = models.IntegerField()
    
    price           = models.IntegerField()

    create_at       = models.DateTimeField(editable=False)
    last_modified   = models.DateTimeField()


    def save(self, *args, **kwargs):
        '''On save, update/fill fields.'''

        self.last_modified = timezone.now()

        return super(Product, self).save(*args, **kwargs)


    def __str__(self):
        return self.brand.name + ' ' + self.name


