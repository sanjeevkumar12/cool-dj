from django.views.generic import FormView,RedirectView
from .mixins import LoginRequiredMixin
from ..forms import RegistrationForm,AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as __
from django.contrib import messages
from django.contrib.auth import logout as auth_logout,login as auth_login
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('accounts:login')
    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        user.sendactivationmail(self.request)
        messages.add_message(self.request,messages.INFO,__('Registration Successfull ! A email has been sent to %s. Please verify your account.' % (user.email,)))
        return super(RegisterView,self).form_valid(form)

class LogoutView(LoginRequiredMixin,RedirectView):
    url = reverse_lazy('accounts:login')
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView,self).get(request, *args, **kwargs)

class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy("accounts:profile")

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request,form.get_user())
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
        if(self.request.POST.get('remember_me',None)):
            self.request.session.set_expiry(0)
        return super(LoginView,self).form_valid(form)
    def form_invalid(self, form):
        return super(LoginView,self).form_invalid(form)