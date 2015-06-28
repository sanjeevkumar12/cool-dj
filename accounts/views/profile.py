from .mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy
from ..forms import ImageChangeForm,UserChangeForm
from django.views.generic import FormView
from django.contrib.auth import get_user_model
from django.contrib import messages


class DashBoardView(LoginRequiredMixin,TemplateView):
    template_name = 'accounts/dashboard.html'
    def get_context_data(self, **kwargs):
        context = super(DashBoardView,self).get_context_data(**kwargs)
        return context
class HomeView(TemplateView):
    template_name = "accounts/home.html"

class ChangeprofilePic(LoginRequiredMixin,FormView):
    form_class = ImageChangeForm
    success_url = reverse_lazy("accounts:profile")
    template_name = "accounts/changeprofilepic.html"

    def form_valid(self, form):
        usermodel = get_user_model()
        user = usermodel.objects.get(pk=self.request.user.pk)
        profilepic = form.cleaned_data['profilepic']
        user.image = profilepic
        user.save()
        return super(ChangeprofilePic,self).form_valid(form)

class ProfileView(LoginRequiredMixin,UpdateView):
    model = get_user_model()
    template_name = "accounts/profile.html"
    form_class = UserChangeForm
    success_url = reverse_lazy('accounts:profile')
    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.add_message(self.request,messages.INFO,__("Profile updated successfully."))
        self.request.session.modified = True
        return super(ProfileView,self).form_valid(form)