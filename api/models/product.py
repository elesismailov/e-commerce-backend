from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

from random import randint as r

from api.helpers.generate_slug import generate_slug

# Create your models here.

class Product(models.Model):

    name            = models.CharField(max_length=50)
    description     = models.CharField(max_length=250)
    
    slug            = models.CharField(max_length=50, blank=True, unique=True)

    # TODO how to change category if the category/brand was deleted
    #   (on_delete='do something with the category')
    category        = models.ForeignKey('api.Category', on_delete=models.DO_NOTHING)
    brand           = models.ForeignKey('api.Brand', on_delete=models.DO_NOTHING)

    in_stock_amount = models.IntegerField()
    sold_amount     = models.IntegerField(default=0)
    
    price           = models.IntegerField()

    created_at      = models.DateTimeField(editable=False)
    last_modified   = models.DateTimeField(editable=False)


    def save(self, *args, **kwargs):
        '''On save, update/fill fields.'''

        # First save/creation
        if not self.id:

            self.created_at = timezone.now()

        # Everything happenning below runs every update

        slug = generate_slug(
                self.brand.name,
                self.name,
                self.id or r(0, 1000000000000),
                )


        # if slug somehow exists in the db, regenerate
        while len(Product.objects.filter(slug=slug)) != 0:
            slug = generate_slug(
                    self.brand.name,
                    self.name,
                    self.id or r(0, 10000000000000),
                    )

        self.slug = slug

        self.last_modified = timezone.now()

        return super(Product, self).save(*args, **kwargs)


    def __str__(self):
        return self.brand.name + ' ' + self.name


