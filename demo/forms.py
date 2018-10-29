import django.forms as forms
from .models import Book


class PersonForm(forms.Form):
    fullname = forms.CharField(max_length=30, required=True, label="Fullname")
    email = forms.CharField(max_length=50, required=False, label="Email Address")
    mobile = forms.CharField(max_length=30, required=False, label="Mobile Number")
    age = forms.IntegerField(required=False)


class AddPublisherForm(forms.Form):
    pubname = forms.CharField(max_length=30, required=True, label="Publisher Name")
    website = forms.CharField(max_length=50, required=True, label="Publisher Website")


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
