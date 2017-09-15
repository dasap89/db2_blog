import account.forms
import account.views
import accounts.forms 
import uuid


class LoginView(account.views.LoginView):

    form_class = account.forms.LoginEmailForm


class SignupView(account.views.SignupView):

    form_class = accounts.forms.SignupForm
    identifier_field = 'email'

    def generate_username(self, form):
        # do something to generate a unique username (required by the
        # Django User model, unfortunately)
        
        username = form.cleaned_data['email']
        return username