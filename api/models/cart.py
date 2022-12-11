from django.db import models
from django.utils import timezone

# Create your models here.

class Cart(models.Model):

    customer        = models.ForeignKey('api.Customer', on_delete=models.CASCADE)

    created_at      = models.DateTimeField(editable=False)
    last_modified   = models.DateTimeField()

    def save(self, *args, **kwargs):
        '''On save, update/fill fields.'''

        # First save/creation
        if not self.id:

            self.created_at = timezone.now()

        # Everything happenning below runs every update


        self.last_modified = timezone.now()

        return super(Cart, self).save(*args, **kwargs)














