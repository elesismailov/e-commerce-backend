from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

from api.helpers.generate_slug import generate_slug

# Create your models here.

class Product(models.Model):

    name            = models.CharField(max_length=50)
    description     = models.CharField(max_length=250)
    
    slug            = models.CharField(max_length=50)

    # TODO how to change category if the category/brand was deleted
    #   (on_delete='do something with the category')
    category        = models.ForeignKey('api.Category', on_delete=models.DO_NOTHING)
    brand           = models.ForeignKey('api.Brand', on_delete=models.DO_NOTHING)

    in_stock_amount = models.IntegerField()
    sold_amount     = models.IntegerField()
    
    price           = models.IntegerField()

    created_at      = models.DateTimeField(editable=False)
    last_modified   = models.DateTimeField()


    def save(self, *args, **kwargs):
        '''On save, update/fill fields.'''

        # First save/creation
        if not self.id:

            self.created_at = timezone.now()

        # Everything happenning below runs every update

        self.slug = generate_slug(
                self.brand.name,
                self.name,
                self.id,
                ) or generate_slug(self.name)

        self.last_modified = timezone.now()

        return super(Product, self).save(*args, **kwargs)


    def __str__(self):
        return self.brand.name + ' ' + self.name


