from django.conf.urls import url
from . import views

from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'detail/(?P<slug>[-\w]+)^$',views.DetailView.as_view(),name='blogdetail'),

    ]
