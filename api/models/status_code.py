from django.db import models
from django.utils import timezone

class StatusCode(models.Model):

    code          = models.IntegerField()
    name          = models.CharField(max_length=50)
    description   = models.CharField(max_length=250)

    created_at    = models.DateTimeField(editable=False)
    last_modified = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        '''On save, update/fill fields.'''

        # First save/creation
        if not self.id:
            self.created_at = timezone.now()

        # Everything happenning below runs every update

        self.last_modified = timezone.now()

        return super(StatusCode, self).save(*args, **kwargs)
