from django.db import models
from django.utils import timezone

from api.helpers.generate_slug import generate_slug

# Create your models here.

class Category(models.Model):
    name            = models.CharField(max_length=50)
    description     = models.CharField(max_length=250)
    
    slug            = models.CharField(max_length=50, blank=True)

    parent_category = models.ForeignKey('api.Category', on_delete=models.DO_NOTHING, blank=True, null=True)

    created_at      = models.DateTimeField(editable=False)
    last_modified   = models.DateTimeField()

    def save(self, *args, **kwargs):
        '''On save, update/fill fields.'''

        # First save/creation
        if not self.id:

            self.created_at = timezone.now()

        # Everything happenning below runs every update

        # generating slug
        self.slug = generate_slug(
                [c.name for c in self.get_all_parents()],
                self.name,
                ) or generate_slug(self.name)

        self.last_modified = timezone.now()

        return super(Category, self).save(*args, **kwargs)


    # parent traversion
    def get_all_parents(self):

        if self.parent_category == None:
            return []

        parents = [self.parent_category]

        return self.parent_category.get_all_parents() + parents


    def __str__(self):
        return self.name













