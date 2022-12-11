from django.db import models
from django.utils import timezone

from api.helpers.generate_slug import generate_slug

# Create your models here.

class Brand(models.Model):
    name            = models.CharField(max_length=50)
    description     = models.CharField(max_length=250)
    
    slug            = models.CharField(max_length=50, blank=True)

    created_at      = models.DateTimeField(editable=False)
    last_modified   = models.DateTimeField(editable=False)


    def save(self, *args, **kwargs):
        '''On save, update/fill fields.'''

        # First save/creation
        if not self.id:

            self.created_at = timezone.now()

        # Everything happenning below runs every update

        self.slug = generate_slug(
                'brand',
                self.name,
                ) or generate_slug(self.name)

        self.last_modified = timezone.now()

        return super(Brand, self).save(*args, **kwargs)

    def __str__(self):

        return self.name
