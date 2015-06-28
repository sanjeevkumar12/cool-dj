from django.conf.urls import url
from . import views
from django.core.urlresolvers import reverse_lazy
urlpatterns = [
        url(r'^login$',views.LoginView.as_view(),name='login'),
        url(r'^logout',views.LogoutView.as_view(),name='logout'),
        url(r'^register$',views.RegisterView.as_view(),name='signup'),
        url(r'^dashboard$',views.DashBoardView.as_view(),name='dashboard'),
        url(r'^verifyeaccount$',views.ResendConfirmationLinkView.as_view(),name='reconfirm'),
        url(r'^profile(?:/(?P<file_upload>[a-zA-Z]+))?$',views.ProfileView.as_view(),name='profile'),
        url(r'^confirm/(?P<userslug>[-\w]+)/(?P<activationkey>[-\w]+)$',views.EmailConfirmation.as_view(),name='emailconfirmation'),
        url(r'^password/post-passwordchange$',views.ChangePasswordView.as_view(),name='postpasswordchange'),
        url(r'^password/changepassword$', 'django.contrib.auth.views.password_change', {'post_change_redirect' : reverse_lazy('accounts:postpasswordchange'),'template_name': 'accounts/changepassword.html'},name='changepassword'),
        url(r'^profieimage',views.ChangeprofilePic.as_view(),name='changeprofilepic'),
]
