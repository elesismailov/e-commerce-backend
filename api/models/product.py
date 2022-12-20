from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

from random import randint as r

from api.helpers.generate_slug import generate_slug

# Create your models here.

class Product(models.Model):

    name            = models.CharField(max_length=50)
    description     = models.CharField(max_length=250, blank=True, default='')
    slug            = models.CharField(max_length=250, blank=True, unique=True)
    # TODO how to change category if the category/brand was deleted
    #   (on_delete='do something with the category')
    category        = models.ForeignKey('api.Category', on_delete=models.DO_NOTHING)
    brand           = models.ForeignKey('api.Brand', on_delete=models.DO_NOTHING)

    is_active       = models.BooleanField(default=True)
    price           = models.DecimalField(max_digits=10, decimal_places=3, default=0, blank=True)

    created_at      = models.DateTimeField(editable=False)
    last_modified   = models.DateTimeField(editable=False)


    def save(self, *args, **kwargs):
        '''On save, update/fill fields.'''

        # First save/creation
        if not self.id:

            self.created_at = timezone.now()

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
        # Everything happenning below runs every update


        self.last_modified = timezone.now()

        return super(Product, self).save(*args, **kwargs)


    def __str__(self):
        return self.brand.name + ' ' + self.name




class Variant(models.Model):

    # e.g. SIZE, COLOR
    name            = models.CharField(max_length=50)
    product         = models.ForeignKey('api.Product', on_delete=models.CASCADE)

    created_at      = models.DateTimeField(editable=False)
    last_modified   = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        '''On save, update/fill fields.'''
        # First save/creation
        if not self.id:
            self.created_at = timezone.now()
        self.last_modified = timezone.now()
        return super(Variant, self).save(*args, **kwargs)

    def __str__(self):
        return self.product.name + ' ' + self.name


class VariantOption(models.Model):

    # e.g. SIZE - XS, S, M, L
    name            = models.CharField(max_length=50)
    variant         = models.ForeignKey('api.Variant', on_delete=models.CASCADE)

    created_at      = models.DateTimeField(editable=False)
    last_modified   = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        '''On save, update/fill fields.'''
        if not self.id:
            self.created_at = timezone.now()
        self.last_modified = timezone.now()
        return super(VariantOption, self).save(*args, **kwargs)

    def __str__(self):
        return self.variant.product.name + ' ' + self.variant.name + ' ' + self.name


class Sku(models.Model):

    name           = models.CharField(max_length=100, blank=True, null=True)
    product        = models.ForeignKey('api.Product', on_delete=models.CASCADE)
    barcode        = models.CharField(max_length=100, unique=True, blank=True)
    price          = models.DecimalField(max_digits=10, decimal_places=3)

    slug           = models.CharField(max_length=250, blank=True, unique=True)

    in_stock       = models.DecimalField(max_digits=10, decimal_places=3, default=0)

    created_at     = models.DateTimeField(editable=False)
    last_modified  = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        '''On save, update/fill fields.'''
        if not self.id:
            self.created_at = timezone.now()

            barcode = r(0, 1000000000000)

            # if slug somehow exists in the db, regenerate
            while len(Sku.objects.filter(barcode=barcode)) != 0:
                barcode = r(0, 1000000000000)

            self.barcode = barcode
            self.slug    = generate_slug(self.product.slug, self.barcode)

        self.last_modified = timezone.now()
        return super(Sku, self).save(*args, **kwargs)

    def __str__(self):
        return self.product.name + ' ' + self.barcode

class SkuMapper(models.Model):

    sku = models.ForeignKey('api.Sku', on_delete=models.CASCADE)
    variant_option  = models.ForeignKey('api.VariantOption', on_delete=models.CASCADE)

    created_at      = models.DateTimeField(editable=False)
    last_modified   = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        '''On save, update/fill fields.'''
        if not self.id:
            self.created_at = timezone.now()
        self.last_modified = timezone.now()
        return super(SkuMapper, self).save(*args, **kwargs)

    def __str__(self):
        return 'Mapper ' + self.sku.product.name + ' ' + self.variant_option.variant.name + ' ' + self.variant_option.name













