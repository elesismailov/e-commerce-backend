from django.db import models
from django.utils import timezone

# Create your models here.

class CartItem(models.Model):

    customer         = models.ForeignKey('api.Customer', on_delete=models.CASCADE)

    product          = models.ForeignKey('api.Product', on_delete=models.CASCADE)

    quantity         = models.IntegerField()

    # price_expires_at = models.DateTimeField()

    is_active        = models.BooleanField(default=True)

    created_at       = models.DateTimeField(editable=False)
    last_modified    = models.DateTimeField(editable=False)

    deleted_at       = models.DateTimeField(null=True, blank=True)

    checked_out_at   = models.DateTimeField(null=True, blank=True) 

    def save(self, *args, **kwargs):
        '''On save, update/fill fields.'''

        # First save/creation
        if not self.id:

            self.created_at = timezone.now()

        # Everything happenning below runs every update

        # if self.is_active:


        self.last_modified = timezone.now()

        return super(CartItem, self).save(*args, **kwargs)










