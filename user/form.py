from django.contrib.auth.forms import UserCreationForm, forms
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    full_name = forms.CharField(max_length=30)
    contact_number = forms.IntegerField()
   # lname = forms.CharField(max_length=10)

    class Meta:
        model = User
        fields = ['username',
                  'full_name',
                  'email',
                  'contact_number',
                  'password1',
                  'password2',

        ]

