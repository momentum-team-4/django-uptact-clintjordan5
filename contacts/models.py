from django.db import models
from django.core.validators import RegexValidator
from localflavor.us.models import USStateField, USZipCodeField
from users.models import User
# added user import 


class Contact(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?\d{10}$',
        message="Phone number must be entered in the format: '+9999999999'.")

    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=11,
                                    validators=[phone_regex],
                                    null=True,
                                    blank=True)
    address_1 = models.CharField(max_length=255, null=True, blank=True)
    address_2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = USStateField(null=True, blank=True)
    zip_code = USZipCodeField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    """
    added user with foreign key
    """
    # added birthday line, used commands
    # python3 manage.py makemigrations
    # python3 manage.py migrate

"""
Add a new model, Note, to the contacts app. 
This model should contain text for the note and the date/time of the note. 
Look at the auto_now_add option for the DateTimeField to have the date/time automatically populated.
"""
class Note(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField(auto_add_now=False, null=False, blank-True)
    notes = models.ForeignKey(Contacts, on_delete=models.CASCADE)
# making new note model

