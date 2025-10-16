from django import forms
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User


USER_TYPE = [
    ("Doctor", "Doctor"),
    ("Patient", "Patient"),
]


class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'John Doe'}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'johndoe@gmail.com'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '*************'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '*************'}))
    user_type = forms.ChoiceField(
        choices=USER_TYPE, widget=forms.Select(attrs={"class": "form-select"}))

    class Meta:
        model = User
        fields = ['full_name', 'email', 'password1', 'password2', 'user_type']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove password validators to accept weak passwords
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = 'Enter the same password as before, for verification.'
    
    def clean_password1(self):
        # Override to skip password validation
        password1 = self.cleaned_data.get('password1')
        return password1
    
    def _post_clean(self):
        # Override to skip password validation
        super(UserCreationForm, self)._post_clean()
        password1 = self.cleaned_data.get('password1')
        if password1:
            try:
                # Skip password validation
                pass
            except Exception:
                pass


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'johndoe@gmail.com'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': '*************'}))

    class Meta:
        model = User
        fields = ['email', 'password']
