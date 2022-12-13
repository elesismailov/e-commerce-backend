from django.db import models
from django.utils import timezone

# Create your models here.

class CartItem(models.Model):

    customer         = models.ForeignKey('api.Customer', on_delete=models.CASCADE)

    product          = models.ForeignKey('api.Product', on_delete=models.CASCADE)

    quantity         = models.IntegerField(default=0)

    # price_expires_at = models.DateTimeField()

    is_active        = models.BooleanField(default=True)

    created_at       = models.DateTimeField(editable=False)
    last_modified    = models.DateTimeField(editable=False)

    checked_out_at   = models.DateTimeField(null=True, blank=True) 

    def save(self, *args, **kwargs):
        '''On save, update/fill fields.'''

        # First save/creation
        if not self.id:

            self.created_at = timezone.now()

        # Everything happenning below runs every update

        if not self.is_active:
            self.checked_out_at = timezone.now()

        self.last_modified = timezone.now()

        return super(CartItem, self).save(*args, **kwargs)

    def __str__(self):
        return self.product.name + ' - ' + str(self.quantity) + 'pc ' + ('Active' if self.is_active else 'Inactive')










