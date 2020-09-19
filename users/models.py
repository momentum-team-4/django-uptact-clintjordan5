from django.db import models
from django.contrib.auth.models import AbstractUser

# Consider creating a custom user model from scratch as detailed at
# https://docs.djangoproject.com/en/3.0/topics/auth/customizing/#specifying-a-custom-user-model


class User(AbstractUser):
    # birthday = models.DateField()
    # looked at custom user model link, tried the code above
    # possibly import AbstracrUser in models.py contacts?
    pass

    
# class Note() placeholder
"""
Add a new model, Note, to the contacts app. 
This model should contain text for the note and the date/time of the note. 
Look at the auto_now_add option for the DateTimeField to have the date/time automatically populated.
Connect the Note model to the Contact model using a ForeignKey.
Use the Django console to add a note to one of your contacts.
Make a new view and template to see an individual contact. 
The URL for this view should be contacts/<int:pk>/. Show the notes for that contact on this individual view. 
Otherwise, this page can look like an individual contact on the contacts list page.
"""