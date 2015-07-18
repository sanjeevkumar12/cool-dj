from django.conf.urls import url
from .views.details import SlugDetailView

from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'detail/(?P<slug>[-\w]+)^$',SlugDetailView.as_view(),name='postsslugdetail'),

    ]
