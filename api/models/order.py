from django.db import models
from django.utils import timezone

class Order(models.Model):

    customer         = models.ForeignKey('api.Customer', on_delete=models.DO_NOTHING)

    customer_comment = models.CharField(max_length=500, blank=True)
    
    status_code      = models.ForeignKey('api.StatusCode', on_delete=models.DO_NOTHING)

    # total            = models.IntegerField()

    created_at       = models.DateTimeField(editable=False)
    last_modified    = models.DateTimeField(editable=False)



    def save(self, *args, **kwargs):
        '''On save, update/fill fields.'''

        # First save/creation
        if not self.id:
            self.created_at = timezone.now()

        # Everything happenning below runs every update

        self.last_modified = timezone.now()

        return super(Order, self).save(*args, **kwargs)
