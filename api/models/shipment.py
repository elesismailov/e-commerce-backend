from django.db import models
from django.utils import timezone

class Shipment(models.Model):

    order           = models.ForeignKey('api.Order', on_delete=models.DO_NOTHING)

    tracking_number = models.IntegerField()

    address_to      = models.CharField(max_length=100)
    address_from    = models.CharField(max_length=100)

    created_at      = models.DateTimeField(editable=False)
    last_modified   = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        '''On save, update/fill fields.'''

        # First save/creation
        if not self.id:
            self.created_at = timezone.now()

        # Everything happenning below runs every update

        self.last_modified = timezone.now()

        return super(Shipment, self).save(*args, **kwargs)

    def __str__(self):
        return 'Shipment ' + self.order
