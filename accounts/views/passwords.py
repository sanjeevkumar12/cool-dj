from .mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as __
from django.views.generic import RedirectView
from django.contrib import messages

class ChangePasswordView(LoginRequiredMixin,RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        messages.add_message(self.request,messages.INFO,__("Password updated successfully"))
        return reverse_lazy("accounts:profile")