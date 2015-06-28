from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^login$',views.LoginView.as_view(),name='login'),
        url(r'^logout',views.LogoutView.as_view(),name='logout'),
        url(r'^register$',views.RegisterView.as_view(),name='signup'),
        url(r'^dashboard$',views.DashBoardView.as_view(),name='dashboard'),
        url(r'^verifyeaccount$',views.ResendConfirmationLinkView.as_view(),name='reconfirm'),
        url(r'^profile$',views.ProfileView.as_view(),name='profile'),
        url(r'^confirm/(?P<userslug>[-\w]+)/(?P<activationkey>[-\w]+)',views.EmailConfirmation.as_view(),name='emailconfirmation'),

]
