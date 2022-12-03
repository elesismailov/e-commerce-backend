
from django.db import models
from django.utils import timezone

# Create your models here.

class Customer(models.Model):

    name          = models.CharField(max_length=50)
    password      = models.CharField(max_length=300)
    email         = models.EmailField(max_length=100, unique=True)
    phone         = models.CharField(max_length=30, unique=True)

    created_at    = models.DateTimeField(editable=False)
    last_modified = models.DateTimeField()

    api_key       = models.CharField(max_length=100)


    def save(self, *args, **kwargs):
        '''On save, update/create fields.'''

        # First save/creation
        if not self.id:

            self.created_at = timezone.now()

        # Updating api_key on any change
        api_key = 'generate_api_key()'
        # if api_key somehow exists in the db, regenerate
        while len(Customer.objects.filter(api_key=api_key)) != 0:
            api_key = 'generate_api_key()'

        self.api_key = api_key

        # Updating last modified
        self.last_modified = timezone.now()

        return super(Customer, self).save(*args, **kwargs)


    def __str__(self):
        return self.name, self.email, self.phone








