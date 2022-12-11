from django.db import models
from django.utils import timezone

# Create your models here.

class CartItem(models.Model):

    cart             = models.ForeignKey('api.Cart', on_delete=models.CASCADE)
    product          = models.ForeignKey('api.Product', on_delete=models.CASCADE)

    quantity         = models.IntegerField()

    price_expires_at = models.DateTimeField(editable=False)

    created_at       = models.DateTimeField(editable=False)
    last_modified    = models.DateTimeField()

    deleted_at       = models.DateTimeField(null=True)

    checked_out_at   = models.DateTimeField(null=True) 

    def save(self, *args, **kwargs):
        '''On save, update/fill fields.'''

        # First save/creation
        if not self.id:

            self.created_at = timezone.now()

        # Everything happenning below runs every update


        self.last_modified = timezone.now()

        return super(Cart, self).save(*args, **kwargs)










