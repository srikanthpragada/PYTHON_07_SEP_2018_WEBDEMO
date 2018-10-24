import django.forms as forms


class PersonForm(forms.Form):
    fullname = forms.CharField(max_length=30, required=True, label="Fullname")
    email = forms.CharField(max_length=50, required=False, label="Email Address")
    mobile = forms.CharField(max_length=30, required=False, label="Mobile Number")
    age = forms.IntegerField(required=False)
