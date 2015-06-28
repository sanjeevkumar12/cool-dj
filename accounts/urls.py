from django.conf.urls import url
from .views import auth,verificationlinks,profile,passwords
from django.core.urlresolvers import reverse_lazy
urlpatterns = [
        url(r'^login$',auth.LoginView.as_view(),name='login'),
        url(r'^logout',auth.LogoutView.as_view(),name='logout'),
        url(r'^register$',auth.RegisterView.as_view(),name='signup'),
        url(r'^dashboard$',profile.DashBoardView.as_view(),name='dashboard'),
        url(r'^verifyeaccount$',verificationlinks.ResendConfirmationLinkView.as_view(),name='reconfirm'),
        url(r'^profile(?:/(?P<file_upload>[a-zA-Z]+))?$',profile.ProfileView.as_view(),name='profile'),
        url(r'^confirm/(?P<userslug>[-\w]+)/(?P<activationkey>[-\w]+)$',verificationlinks.EmailConfirmation.as_view(),name='emailconfirmation'),
        url(r'^password/post-passwordchange$',passwords.ChangePasswordView.as_view(),name='postpasswordchange'),
        url(r'^password/changepassword$', 'django.contrib.auth.views.password_change', {'post_change_redirect' : reverse_lazy('accounts:postpasswordchange'),'template_name': 'accounts/changepassword.html'},name='changepassword'),
        url(r'^profileimage',profile.ChangeprofilePic.as_view(),name='changeprofilepic'),
        url(r'^password/forgotpassword$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : reverse_lazy('accounts:postpasswordresetdone'),
                                                                                       'template_name': 'accounts/forgotpassword.html',
                                                                                       'email_template_name':'accounts/email/forgotpassword.html',
                                                                                        'subject_template_name':'accounts/email/forgotpassword.txt',
                                                                                       },name='forgotpassword'),
        url(r'^password/reset-done$',passwords.ForgotpasswordView.as_view(),name='postpasswordresetdone'),
        url(r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$','django.contrib.auth.views.password_reset_confirm',{
                                                                                        'post_reset_redirect' : reverse_lazy('accounts:login'),
                                                                                        'template_name': 'accounts/resetpassword.html',
                                                                            },name="resetpassword"),
]
