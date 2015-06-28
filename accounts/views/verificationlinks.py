from django.views.generic import TemplateView,FormView
from django.contrib.auth import get_user_model
from django.utils import timezone
from ..forms import ResendActivationLink
from django.core.urlresolvers import reverse_lazy

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
        return super(ResendConfirmationLinkView,self).form_valid(form)