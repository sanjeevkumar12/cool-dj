from django import forms
from django.utils.translation import ugettext_lazy as __
from django.contrib.auth import get_user_model,authenticate
class RegistrationForm (forms.ModelForm):
    password1 = forms.CharField(label = __('Password'),widget=forms.PasswordInput)
    password2 = forms.CharField(label = __('Confirm Password'),widget=forms.PasswordInput)
    firstname = forms.CharField(label=__('First Name'),required= True)

    class Meta:
        model = get_user_model()
        fields = ('email','firstname','lastname','user_bio',)
        widgets = {
            'user_bio': forms.Textarea(attrs={'cols': 80, 'rows': 20}),

        }
        error_messages = {
            'email': {
                'required': __("Please enter valid email address."),
            },
        }

    def clean_email(self):
        User = get_user_model()
        try:
            user = User.objects.get(email__iexact = self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError(__('User with email already exists.'))
    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 != password2:
            raise forms.ValidationError(__('Passwords donot match.'))
        return password2
    def save(self, commit=True):
        user = super(RegistrationForm,self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit :
            user.save()
        return user

class AuthenticationForm(forms.Form):

    email = forms.EmailField(label= __("Email"),required=True)
    password = forms.CharField(label=__("Password"), widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())

    error_messages = {
        'invalid_login': __("Please enter a correct email and password. "),
        'inactive': __("This account is inactive."),
    }

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        UserModel = get_user_model()
        self.username_field = UserModel._meta.get_field(UserModel.USERNAME_FIELD)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        if email and password:
            self.user_cache = authenticate(username=email,password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'email': self.username_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

    def get_user_id(self):
        if self.user_cache:
            return self.user_cache.id
        return None

    def get_user(self):
        return self.user_cache

class ResendActivationLink(forms.Form):

    email = forms.EmailField(label='Email Address',required=True)

    error_messages = {
        'activeuser': __("User already active . "),
        'usernotfound': __("User with this email not found . "),
    }

    def __init__(self,*args, **kwargs):
        self.user_cache = None
        super(ResendActivationLink, self).__init__(*args, **kwargs)
        self.usermodel = get_user_model()
        self.username_field = self.usermodel._meta.get_field(self.usermodel.USERNAME_FIELD)

    def clean_email(self):
        try:
            self.user_cache = self.usermodel.objects.get(email__iexact = self.cleaned_data['email'])
            if self.user_cache.is_active :
                raise forms.ValidationError(
                    self.error_messages['activeuser'],
                    code='activeuser',
                    params={'email': self.username_field.verbose_name},
                )
        except self.usermodel.DoesNotExist:
                raise forms.ValidationError(
                    self.error_messages['usernotfound'],
                    code='usernotfound',
                    params={'email': self.username_field.verbose_name},
                )
        return self.cleaned_data['email']
    def resendActivationLink(self,request):
        if self.user_cache :
            self.user_cache.sendactivationmail(request)

    def getuser(self):
        return self.user_cache


class UserChangeForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        fields = ('firstname','lastname','user_bio',)
        widgets = {
            'user_bio': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }
