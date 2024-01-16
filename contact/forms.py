from django import forms
from django.core.exceptions import ValidationError
from contact.models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import password_validation
from django.contrib.auth import get_user_model


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ContactForm(forms.ModelForm):
    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Escreva aqui',
    #         }
    #     ),
    #     label = 'Primeiro nome',
    #     help_text='campo de ajuda' # dá para por no form um {{field.help_text}}
    # )
    picture = forms.ImageField(
        widget= forms.FileInput(
            attrs={
                'accept': 'image/*',
            }
        ),
        required=False
    )
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
        # self.fields['first_name'].widget.attrs.update(
        #     {'class': 'form-control',
        #      'placeholder': 'Escreva aqui',
        #      }
        # ) #é para modificar o widget do campo, dá para alterar classe por aqui
    
    class Meta:
        model = Contact
        fields = 'first_name','last_name', 'phone', 'email', 'description', 'category', 'picture',
        # widgets = {
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class': 'form-control'
        #         }
        #         )  #é para modificar o widget do campo, dá para alterar classe por aqui
            
        # }
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            self.add_error(
                'last_name',              #se for um None aqui, é um non field error
                ValidationError(
                    'Primeiro nome não pode ser igual ao segundo',
                    code='invalid',
                )
            )
        return super().clean()
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name ==  'ABC':
            self.add_error(
            'first_name',              #se for um None aqui, é um non field error
            ValidationError(
                'Mensagem de erro',
                code='invalid',
            )
            )
        return first_name
    

class RegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    
    first_name = forms.CharField(
        required=True,
        min_length=3
    )
    
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1', 'password2',
        )
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Já existe este e-mail', code= 'invalid')
            )
        
        return email

class RegisterUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RegisterUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    
    first_name = forms.CharField(
        required=True,
        min_length=3,
        max_length=30,
        help_text='Required',
        error_messages={
            'min_length': 'Please, add more than 2 letters'
        }
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
        max_length=30,
        help_text='Required',
        error_messages={
            'min_length': 'Please, add more than 2 letters'
        }
    ) 
    
    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False
    )
    password2 = forms.CharField(
        label="Password 2",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text= 'Use the same password as before',
        required=False
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username',
        )
    
    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')
        
        if password:
            user.set_password(password)
            
        if commit:
            user.save()
        return user
    
    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2', 
                    ValidationError('Senhas não batem')
                )

    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error('password1', ValidationError(errors))
            return password1

    # def clean_password2(self):
    #     # Define um método vazio para evitar o erro de desconhecimento do campo password2
    #     pass
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email
        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Já existe este e-mail', code= 'invalid')
                )
            
        return email