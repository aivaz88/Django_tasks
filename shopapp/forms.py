from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'example@example.ru'}))
    password = forms.CharField(max_length=15, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                               'placeholder': 'Пароль'}))


class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                       'placeholder': 'Имя'}))
    surname = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                          'placeholder': 'Фамилия'}))
    telephone = forms.CharField(max_length=11, required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                            'placeholder': '7-9XX-XXX-XX-XX'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                           'placeholder': 'example@example.ru'}))
    address = forms.CharField(max_length=300, required=True, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                           'placeholder': 'Адресс'}))
    password = forms.CharField(max_length=15, required=True, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                               'placeholder': 'Пароль'}))
