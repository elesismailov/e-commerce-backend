from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

from api.helpers.generate_api_key import generate_api_key

# Create your models here.

class Staff(models.Model):

    name          = models.CharField(max_length=50)
    password      = models.CharField(max_length=300)
    email         = models.EmailField(max_length=100, unique=True)

    created_at    = models.DateTimeField(editable=False)
    last_modified = models.DateTimeField(editable=False)

    api_key       = models.CharField(max_length=100, unique=True)


    def save(self, *args, **kwargs):
        '''On save, update/fill fields.'''

        # First save/creation
        if not self.id:

            # Hashing password
            self.password = make_password(self.password)

            self.created_at = timezone.now()

        # Everything happenning below runs every update

        # Updating api_key on any change
        api_key = generate_api_key()
        # if api_key somehow exists in the db, regenerate
        while len(Customer.objects.filter(api_key=api_key)) != 0:
            api_key = generate_api_key()

        self.api_key = api_key

        self.last_modified = timezone.now()

        return super(Staff, self).save(*args, **kwargs)



    def __str__(self):
        return self.name + ' ' + self.email


