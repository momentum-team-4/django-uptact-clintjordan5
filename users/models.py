from django.db import models
from django.contrib.auth.models import AbstractUser

# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model


class User(AbstractUser):
    # birthday = models.DateField()
    # looked at custom user model link, tried the code above
    # possibly import AbstracrUser in models.py contacts?
    pass

    
    
