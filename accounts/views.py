from django.shortcuts import render,redirect
from .forms import RegistrationForm,AuthenticationForm,ResendActivationLink
from django.views.generic.edit import FormView,UpdateView
from django.views.generic import RedirectView
from django.views.generic import TemplateView,View
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import REDIRECT_FIELD_NAME ,login as auth_login ,logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext_lazy as __
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.contrib.auth import get_user_model
from django.utils import timezone

class LoginRequiredMixin(object):

    @method_decorator(login_required)
    def dispatch(self,*args,**kwargs):
        return super(LoginRequiredMixin,self).dispatch(*args,**kwargs)

class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('accounts:login')
    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        user.sendactivationmail(self.request)
        return super(RegisterView,self).form_valid(form)

class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm
    success_url = "/dashboard"
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.info(self.request,'Welcome back to ')
        auth_login(self.request,form.get_user())
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
        if(self.request.POST.get('remember_me',None)):
            self.request.session.set_expiry(0)
        return super(LoginView,self).form_valid(form)

class LogoutView(LoginRequiredMixin,RedirectView):
    url = reverse_lazy('accounts:login')
    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return super(LogoutView,self).get(request, *args, **kwargs)

class DashBoardView(LoginRequiredMixin,TemplateView):
    template_name = 'accounts/dashboard.html'
    def get_context_data(self, **kwargs):
        context = super(DashBoardView,self).get_context_data(**kwargs)
        return context
class HomeView(TemplateView):
    template_name = "accounts/home.html"

class EmailConfirmation(TemplateView):
    template_name = 'accounts/confirm.html'
    def get_context_data(self,**kwargs):
        context = super(EmailConfirmation,self).get_context_data(**kwargs)
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(slug=kwargs.get('userslug'))
            if user.is_active == False:
                if kwargs['activationkey'] and kwargs['activationkey'] == user.user_hash:
                    if user.hash_expire < timezone.now():
                        context['status'] = 'tokenexpired'
                    else:
                        context['status'] = 'successful'
                        user.is_active = True
                        user.hash_expire = None
                        user.user_hash = ''
                        user.save()
                else:
                    context['status'] = 'invalidtoken'
            else:
                context['status'] = 'invalidlink'
        except UserModel.DoesNotExist:
            context['status'] = 'invalidlink'
        return context
class ResendConfirmationLinkView(FormView):
    template_name = 'accounts/resendeverificatiionmail.html'
    form_class = ResendActivationLink
    success_url = reverse_lazy("accounts:login")
    def form_valid(self, form):
        form.resendActivationLink(self.request)
        return super(FormView,self).form_valid(form)
class ProfileView(LoginRequiredMixin,UpdateView):
    model = get_user_model()
    template_name = "accounts/profile.html"
    def get_object(self, queryset=None):
        return self.request.user

#chandniduggal@hotmail.com/sai_03_04_84