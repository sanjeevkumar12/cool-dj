from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^mycalender$',views.Calender.as_view(),name='usercalender'),
    ]
