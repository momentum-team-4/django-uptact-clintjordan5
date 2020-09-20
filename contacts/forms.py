from django import forms
from .models import Contact
from .models import Note

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'phone_number',
            'email',
            'birthday',
        ]
# added 'birthday' to contact model

"""
Add a new model, Note, to the contacts app. 
This model should contain text for the note and the date/time of the note. 
Look at the auto_now_add option for the DateTimeField to have the date/time automatically populated.
"""

class NoteForm(forms.ModelForm)
    class Meta:
        model = Note
        fields = [
            'text',
            'date',
            'time',
            'notes',
        ]
# making new NoteForm class using concept from Contact class 