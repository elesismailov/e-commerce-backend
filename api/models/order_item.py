from django.db import models
from django.utils import timezone

class OrderItem(models.Model):

    product       = models.ForeignKey('api.Product', on_delete=models.CASCADE)
    
    price         = models.IntegerField()

    quantity      = models.IntegerField(default=1)

    created_at    = models.DateTimeField(editable=False)
    last_modified = models.DateTimeField(editable=False)


    def save(self, *args, **kwargs):
        '''On save, update/fill fields.'''

        # First save/creation
        if not self.id:
            self.created_at = timezone.now()

        # Everything happenning below runs every update

        self.last_modified = timezone.now()

        return super(OrderItem, self).save(*args, **kwargs)
